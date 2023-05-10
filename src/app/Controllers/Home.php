<?php

namespace App\Controllers;

class Home extends BaseController
{
    public function index()
    {

        return view('partial/header', ['title' => 'stat466.home.home'])
                . view('home')
                . view('partial/footer');
    }

    public function setLanguage($language = 'en')
    {
        $this->session->set('setlanguage', $language);
        return redirect()->back();
    }

}
