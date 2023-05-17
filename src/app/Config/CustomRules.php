<?php

namespace Config;

class CustomRules
{
    public function isoldpassword($value, ?string &$error = null): bool
    {
        $result = auth()->check([
            'email'    => auth()->user()->email,
            'password' => $value,
        ]);

        if( !$result->isOK() ) {
            $error = lang('stat466.profile.oldpasswordwrong');
            return false;
        }

        return true;
    }
}