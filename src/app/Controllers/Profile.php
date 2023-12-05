<?php

namespace App\Controllers;

use App\Controllers\BaseController;
use App\Models\UserModel;
use CodeIgniter\Exceptions\PageNotFoundException;

class Profile extends BaseController
{
    public function edit()
    {
        $this->addBreadcrumb('stat466.profile.index', null, true);
        $this->addBreadcrumb('stat466.profile.edit', null, true);
        $usermodel = new UserModel();
        $user = auth()->user();
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

                $usermodel->save($user);
                $this->showMessage(lang('stat466.profile.editsuccess'));
                return redirect()->back();
            }
        }
        $this->data['title'] = 'stat466.profile.edit';
        return view('partial/header', $this->data)
            . view('profile/edit', $data)
            . view('partial/footer');
    }

    public function changepw()
    {
        $this->addBreadcrumb('stat466.profile.index', null, true);
        $this->addBreadcrumb('stat466.profile.changepw', null, true);
        $usermodel = new UserModel();
        $user = auth()->user();
        if (is_null($user))
        {
            throw PageNotFoundException::forPageNotFound();
        }
        $data = [];
        if ($this->request->getMethod() == 'post')
        {
            $input = $this->validate([
                'oldpassword' => [
                    'required',
                    'min_length[1]',
                    'max_length[99]',
                    'isoldpassword'
                ],
                'newpassword' => [
                    'required',
                    'min_length[3]',
                    'max_length[99]',
                    'matches[confirmpassword]'
                ],
                'confirmpassword' => [
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
                $newpassword = $this->request->getVar('newpassword');
                $user->password = $newpassword;

                $usermodel->save($user);
                $this->showMessage(lang('stat466.profile.changepwsuccess'));
                return redirect()->back();
            }
        }
        $this->data['title'] = 'stat466.profile.changepw';
        return view('partial/header', $this->data)
            . view('profile/changepw', $data)
            . view('partial/footer');
    }
}
