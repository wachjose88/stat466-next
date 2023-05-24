<?php

namespace App\Database\Migrations;

use CodeIgniter\Database\Migration;

class League extends Migration
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
                'name' => [
                        'type'       => 'VARCHAR',
                        'constraint' => '100'
                ],
        ]);
        $this->forge->addKey('id', true);
        $this->forge->createTable('leagues');

        $this->forge->addField([
                'id' => [
                        'type'           => 'INT',
                        'constraint'     => 10,
                        'unsigned'       => true,
                        'auto_increment' => true,
                ],
                'user_id' => [
                        'type'           => 'INT',
                        'constraint'     => 10,
                        'unsigned'       => true,
                ],
                'league_id' => [
                        'type'           => 'INT',
                        'constraint'     => 10,
                        'unsigned'       => true,
                ],
                'active' => [
                        'type'           => 'INT',
                        'constraint'     => 10,
                        'unsigned'       => true,
                ],
        ]);
        $this->forge->addKey('id', true);
        $this->forge->createTable('userofleagues');
        $this->forge->addForeignKey('league_id', 'leagues', 'id');
        $this->forge->addForeignKey('user_id', 'users', 'id');
    }

    public function down()
    {
        $this->forge->dropTable('leagues');
        $this->forge->dropTable('userofleagues');
    }
}
