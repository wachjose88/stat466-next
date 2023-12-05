<?php

namespace App\Database\Migrations;

use CodeIgniter\Database\Migration;

class Result2P extends Migration
{
    public function up()
    {
        $this->forge->addField([
            'id' => [
                'type'           => 'INT',
                'constraint'     => 10,
                'unsigned'       => true,
                'auto_increment' => true,
            ],
            'league_id' => [
                'type'           => 'INT',
                'constraint'     => 10,
                'unsigned'       => true,
            ],
            'player_1' => [
                'type'           => 'INT',
                'constraint'     => 10,
                'unsigned'       => true,
            ],
            'player_2' => [
                'type'           => 'INT',
                'constraint'     => 10,
                'unsigned'       => true,
            ],
            'points_p1' => [
                'type'           => 'INT',
                'constraint'     => 10,
                'unsigned'       => true,
            ],
            'points_p2' => [
                'type'           => 'INT',
                'constraint'     => 10,
                'unsigned'       => true,
            ],
            'played_at' => [
                'type'           => 'TIMESTAMP'
            ],
        ]);
        $this->forge->addKey('id', true);
        $this->forge->createTable('result2p');
        $this->forge->addForeignKey('league_id', 'leagues', 'id');
        $this->forge->addForeignKey('player_1', 'users', 'id');
        $this->forge->addForeignKey('player_2', 'users', 'id');
    }

    public function down()
    {
        $this->forge->dropTable('result2p');
    }
}
