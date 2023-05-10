<?php

namespace App\Controllers;

class RegisterController extends \CodeIgniter\Shield\Controllers\RegisterController
{
    protected function getValidationRules(): array {
        $rules = parent::getValidationRules();
        if (is_array($rules)) {
            $rules['first_name'] = [
                    'label' => 'stat466.Auth.first_name',
                    'rules' => 'required'
            ];
            $rules['last_name'] = [
                    'label' => 'stat466.Auth.last_name',
                    'rules' => 'required'
            ];
        }
        return $rules;
    }
}
