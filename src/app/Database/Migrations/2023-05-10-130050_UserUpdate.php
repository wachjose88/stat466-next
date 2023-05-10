<?php

namespace App\Database\Migrations;

use CodeIgniter\Database\Migration;

class UserUpdate extends Migration
{
    public function up()
    {
        $fields = [
                'first_name' => [
                        'type' => 'VARCHAR',
                        'constraint' => 100
                ],
                'last_name' => [
                        'type' => 'VARCHAR',
                        'constraint' => 100
                ]
        ];
        $this->forge->addColumn('users', $fields);
    }

    public function down()
    {
        $this->forge->dropColumn('users', 'first_name');
        $this->forge->dropColumn('users', 'last_name');
    }
}
