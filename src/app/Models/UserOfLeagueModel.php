<?php

namespace App\Models;

use CodeIgniter\Model;

class UserOfLeagueModel extends Model
{
    protected $DBGroup          = 'default';
    protected $table            = 'userofleagues';
    protected $primaryKey       = 'id';
    protected $useAutoIncrement = true;
    protected $returnType       = 'array';
    protected $useSoftDeletes   = false;
    protected $protectFields    = true;
    protected $allowedFields    = ['user_id', 'league_id'];

    // Dates
    protected $useTimestamps = false;
    protected $dateFormat    = 'datetime';
    protected $createdField  = 'created_at';
    protected $updatedField  = 'updated_at';
    protected $deletedField  = 'deleted_at';

    // Validation
    protected $validationRules      = [];
    protected $validationMessages   = [];
    protected $skipValidation       = false;
    protected $cleanValidationRules = true;

    // Callbacks
    protected $allowCallbacks = true;
    protected $beforeInsert   = [];
    protected $afterInsert    = [];
    protected $beforeUpdate   = [];
    protected $afterUpdate    = [];
    protected $beforeFind     = [];
    protected $afterFind      = [];
    protected $beforeDelete   = [];
    protected $afterDelete    = [];

    public function getLeaguesOfUser($userid)
    {
        $leaguemodel = new LeagueModel();
        $userleagues = [];
        $leagues = $this->where('user_id', $userid)->findAll();
        foreach ($leagues as &$league)
        {
            $userleagues[] = $leaguemodel->where('id', $league['league_id'])->first();
        }
        return $userleagues;
    }

    public function getUsersOfLeague($leagueid)
    {
        $usermodel = auth()->getProvider();
        $users = [];
        $userleagues = $this->where('league_id', $leagueid)->findAll();
        foreach ($userleagues as $userleague)
        {
            $users[$userleague['user_id']] = $usermodel->findById($userleague['user_id']);
        }
        return $users;
    }
}
