<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title><?= lang('stat466.home.title'); ?></title>
        <link href="<?= base_url('css/bootstrap.css'); ?>" rel="stylesheet">
    </head>
    <body>
    <nav class="navbar navbar-expand-lg bg-primary navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="<?= base_url('/') ?>">
                <?= lang('stat466.home.title'); ?></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page"
                           href="<?= base_url('/') ?>">
                            <?= lang('stat466.home.home'); ?>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            <?= lang('stat466.language.select'); ?>
                        </a>
                        <ul class="dropdown-menu">
                            <?php foreach (config('App')->supportedLocales as $locale): ?>
                            <li><a class="dropdown-item" href="<?= base_url('setlang/' . $locale) ?>">
                                    <?= lang('stat466.language.' . $locale); ?></a></li>
                            <?php endforeach; ?>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container">