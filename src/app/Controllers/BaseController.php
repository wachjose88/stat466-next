<?php

namespace App\Controllers;

use App\Models\UserOfLeagueModel;
use CodeIgniter\Controller;
use CodeIgniter\HTTP\CLIRequest;
use CodeIgniter\HTTP\IncomingRequest;
use CodeIgniter\HTTP\RequestInterface;
use CodeIgniter\HTTP\ResponseInterface;
use Config\App;
use Psr\Log\LoggerInterface;

/**
 * Class BaseController
 *
 * BaseController provides a convenient place for loading components
 * and performing functions that are needed by all your controllers.
 * Extend this class in any new controllers:
 *     class Home extends BaseController
 *
 * For security be sure to declare any new methods as protected or private.
 */
abstract class BaseController extends Controller
{
    /**
     * Instance of the main Request object.
     *
     * @var CLIRequest|IncomingRequest
     */
    protected $request;

    /**
     * An array of helpers to be loaded automatically upon
     * class instantiation. These helpers will be available
     * to all other controllers that extend BaseController.
     *
     * @var array
     */
    protected $helpers = [];

    /**
     * Be sure to declare properties for any property fetch you initialized.
     * The creation of dynamic property is deprecated in PHP 8.2.
     */
    protected $session;

    protected $data = [];

    /**
     * Constructor.
     */
    public function initController(RequestInterface $request, ResponseInterface $response, LoggerInterface $logger)
    {
        $this->helpers = array_merge($this->helpers, ['setting']);

        // Do Not Edit This Line
        parent::initController($request, $response, $logger);

        // Preload any models, libraries, etc, here.

        $this->session = \Config\Services::session();
        $config = config(App::class);

        $this->data['breadcrumb'] = [];
        $this->addBreadcrumb('stat466.home.home', '/', false);

        $message = $this->session->get('message');
        if (!is_null($message))
        {
            $this->data['message'] = $message;
            $this->data['messagetype'] = $this->session->get('messagetype');
            $this->session->set('message', null);
        }

        $language = $this->session->get('setlanguage');
        $language = is_null($language) ? $config->defaultLocale : $language;
        $this->request->setLocale($language);

        $userofleaguemodel = new UserOfLeagueModel();
        if (!is_null(auth()->user()))
        {
            $this->data['userleagues'] = $userofleaguemodel->getLeaguesOfUser(
                    auth()->user()->id
            );
        }

    }

    protected function showMessage($message, $type = 'success')
    {
        $this->session->set('message', $message);
        $this->session->set('messagetype', $type);
    }

    protected function addBreadcrumb($title, $url, $active)
    {

        $this->data['breadcrumb'][] = [
                'title' => lang($title),
                'url' => is_null($url) ? null : base_url($url),
                'active' => $active
        ];
    }
}
