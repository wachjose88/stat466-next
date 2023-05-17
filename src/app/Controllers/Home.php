<?php

namespace App\Controllers;

class Home extends BaseController
{
    public function index()
    {
        $this->data['title'] = 'stat466.home.home';
        return view('partial/header', $this->data)
                . view('home')
                . view('partial/footer');
    }

    public function setLanguage($language = 'en')
    {
        $this->session->set('setlanguage', $language);
        return redirect()->back();
    }

}
