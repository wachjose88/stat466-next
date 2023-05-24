<?php

namespace App\Database\Migrations;

use CodeIgniter\Database\Migration;

class LeagueActive extends Migration
{
    public function up()
    {
        $this->forge->dropColumn('userofleagues', 'active');
    }

    public function down()
    {
        $this->forge->addColumn('userofleagues', [
            'active' => [
                'type'           => 'INT',
                'constraint'     => 10,
                'unsigned'       => true,
            ]
        ]);
    }
}
