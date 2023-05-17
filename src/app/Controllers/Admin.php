<?php

namespace App\Controllers;

use App\Controllers\BaseController;
use App\Models\UserModel;
use CodeIgniter\Exceptions\PageNotFoundException;

class Admin extends BaseController
{
    public function index()
    {
        $usermodel = new UserModel();
        $users = $usermodel->findAll();
        if (!is_array($users))
        {
            $users = [$users];
        }
        $data = [
                'users' => $users
        ];
        $this->data['title'] = 'stat466.admin.index';
        return view('partial/header', $this->data)
                . view('admin/index', $data)
                . view('partial/footer');
    }

    public function createuser()
    {
        $usermodel = new UserModel();
        $values = [
                'username' => '',
                'first_name' => '',
                'last_name' => '',
                'email' => '',
                'password' => '',
                'groups' => [],
                'active' => 0
        ];
        $data = [
                'groups' => config('Config\AuthGroups')->groups,
                'old' => $values
        ];
        if ($this->request->getMethod() == 'post')
        {
            $input = $this->validate([
                    'username' => [
                            'required',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'first_name' => [
                            'required',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'last_name' => [
                            'required',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'email' => [
                            'required',
                            'valid_email',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'password' => [],
                    'groups' => [
                            'required'
                    ]
            ]);
            $username = $this->request->getVar('username');
            $first_name = $this->request->getVar('first_name');
            $last_name = $this->request->getVar('last_name');
            $email = $this->request->getVar('email');
            $password = $this->request->getVar('password');
            $groups = $this->request->getPost('groups');
            $active = $this->request->getVar('active');
            $values = [
                    'username' => $username,
                    'first_name' => $first_name,
                    'last_name' => $last_name,
                    'email' => $email,
                    'password' => $password,
                    'groups' => $groups,
                    'active' => $active
            ];
            if (!$input)
            {
                $data['validation'] = $this->validator;
                $data['old'] = $values;
            }
            else
            {

                $usermodel->save($values);
                $user = $usermodel->select()->where('username', $username)->first();
                $user->email = $email;
                $usermodel->save($user);
                $user->syncGroups(...$groups);
                $this->showMessage(lang('stat466.admin.users.createsuccess'));
                return redirect()->to('admin');
            }
        }
        $this->data['title'] = 'stat466.admin.users.create';
        return view('partial/header', $this->data)
                . view('admin/user/create', $data)
                . view('partial/footer');
    }

    public function edituser($userid)
    {
        $usermodel = new UserModel();
        $user = $usermodel->findById($userid);
        if (is_null($user))
        {
            throw PageNotFoundException::forPageNotFound();
        }
        $data = [
                'user' => $user,
                'groups' => config('Config\AuthGroups')->groups,
                'usergroups' => $user->getGroups()
        ];
        if ($this->request->getMethod() == 'post')
        {
            $input = $this->validate([
                    'username' => [
                            'required',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'first_name' => [
                            'required',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'last_name' => [
                            'required',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'email' => [
                            'required',
                            'valid_email',
                            'min_length[3]',
                            'max_length[99]'
                    ],
                    'password' => [],
                    'groups' => [
                            'required'
                    ]
            ]);
            if (!$input)
            {
                $data['validation'] = $this->validator;
            }
            else
            {
                $username = $this->request->getVar('username');
                $user->username = $username;
                $first_name = $this->request->getVar('first_name');
                $user->first_name = $first_name;
                $last_name = $this->request->getVar('last_name');
                $user->last_name = $last_name;
                $email = $this->request->getVar('email');
                $user->email = $email;
                $password = $this->request->getVar('password');
                if (!empty($password))
                {
                    $user->password = $password;
                }
                $groups = $this->request->getPost('groups');
                $user->syncGroups(...$groups);
                $active = $this->request->getVar('active');
                $user->active = $active;

                $usermodel->save($user);
                $this->showMessage(lang('stat466.admin.users.editsuccess'));
                return redirect()->to('admin');
            }
        }
        $this->data['title'] = 'stat466.admin.users.edit';
        return view('partial/header', $this->data)
                . view('admin/user/edit', $data)
                . view('partial/footer');
    }

    public function deleteuser($userid)
    {
        $usermodel = new UserModel();
        $usermodel->delete($userid);
        $this->showMessage(lang('stat466.admin.users.deletesuccess'));
        return redirect()->to('admin');
    }
}
