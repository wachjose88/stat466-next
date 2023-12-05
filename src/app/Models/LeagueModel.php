<?php

namespace App\Models;

use CodeIgniter\Model;

class LeagueModel extends Model
{
    protected $DBGroup          = 'default';
    protected $table            = 'leagues';
    protected $primaryKey       = 'id';
    protected $useAutoIncrement = true;
    protected $returnType       = 'array';
    protected $useSoftDeletes   = false;
    protected $protectFields    = true;
    protected $allowedFields    = ['name', 'created_at'];

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

    public function getLeagues()
    {
        $leagues = $this->findAll();
        $userofleaguemodel = new UserOfLeagueModel();
        foreach ($leagues as &$league)
        {
            $league['users'] = $userofleaguemodel->select()->where(
                'league_id', $league['id'])->findAll();
        }
        return $leagues;
    }

    public function getLeague($leagueid)
    {
        $league = $this->find($leagueid);
        $userofleaguemodel = new UserOfLeagueModel();
        $usermodel = auth()->getProvider();
        $league['users'] = $userofleaguemodel->select()->where(
            'league_id', $league['id'])->findAll();
        foreach ($league['users'] as &$user)
        {
            $user['profile'] = $usermodel->findById($user['user_id']);
        }
        return $league;
    }
}
