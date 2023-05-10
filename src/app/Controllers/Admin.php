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
        return view('partial/header', ['title' => 'stat466.admin.index'])
                . view('admin/index', $data)
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
                'user' => $user
        ];
        if ($this->request->getMethod() == 'post')
        {
            $input = $this->validate([
                    'username' => [
                            'required',
                            'min_length[3]',
                            'max_length[99]'
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
                $usermodel->save($user);
                return redirect()->to('admin');
            }
        }
        return view('partial/header', ['title' => 'stat466.admin.users.edit'])
                . view('admin/user/edit', $data)
                . view('partial/footer');
    }
}
