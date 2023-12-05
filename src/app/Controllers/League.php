<?php

namespace App\Controllers;

use App\Controllers\BaseController;
use App\Models\LeagueModel;

class League extends BaseController
{
    public function index($leagueid)
    {
        $leaguemodel = new LeagueModel();
        $league = $leaguemodel->getLeague($leagueid);
        $this->addBreadcrumb('stat466.leagues.index', "league/$leagueid", false);
        $this->addBreadcrumb($league['name'], null, true);
        $data = [
            'league' => $league,
            'league_id' => $leagueid
        ];
        $this->data['title'] = $league['name'];
        return view('partial/header', $this->data)
            . view('league/index', $data)
            . view('partial/footer');
    }

    public function create_result_2p($leagueid)
    {
        $leaguemodel = new LeagueModel();
        $usermodel = auth()->getProvider();
        $league = $leaguemodel->getLeague($leagueid);
        $this->addBreadcrumb('stat466.leagues.index', "league/$leagueid", false);
        $this->addBreadcrumb($league['name'], null, true);
        $this->addBreadcrumb('stat466.leagues.create_result_2p', null, true);
        $values = [
                'player1' => 0,
                'points_p1' => 0,
                'player2' => 0,
                'points_p2' => 0,
                'num_games' => 0
        ];
        $data = [
                'old' => $values,
                'league' => $league,
                'league_id' => $leagueid
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
        $data = [
                'league' => $league,
                'league_id' => $leagueid
        ];
        $this->data['title'] = lang('stat466.leagues.create_result_2p') . ' ' . $league['name'];
        return view('partial/header', $this->data)
                . view('league/create_result_2p', $data)
                . view('partial/footer');
    }
}
