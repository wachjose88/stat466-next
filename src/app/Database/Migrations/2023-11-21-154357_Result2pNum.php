<?php

namespace App\Database\Migrations;

use CodeIgniter\Database\Migration;

class Result2pNum extends Migration
{
    public function up()
    {
        $this->forge->addColumn('result2p',
                ['num_games' => [
                    'type'           => 'INT',
                    'constraint'     => 10,
                    'unsigned'       => true,
            ]]);
    }

    public function down()
    {
        $this->forge->dropColumn('result2p', 'num_games');
    }
}
