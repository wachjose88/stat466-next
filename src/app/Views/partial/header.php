<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>
            <?php if (str_starts_with('stat466.', $title)) { echo lang($title); } else { echo $title; } ?>
            - <?= lang('stat466.home.title'); ?></title>
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
                    <?php if (in_array('admin', auth()->user()->getGroups())): ?>
                    <li class="nav-item">
                        <a class="nav-link"
                           href="<?= base_url('admin') ?>">
                            <?= lang('stat466.admin.index'); ?>
                        </a>
                    </li>
                    <?php endif; ?>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            <?= lang('stat466.leagues.index'); ?>
                        </a>
                        <ul class="dropdown-menu">
                            <?php foreach ($userleagues as $userleague): ?>
                                <li><a class="dropdown-item" href="<?= base_url('league/' . $userleague['id']) ?>">
                                        <?= esc($userleague['name']); ?></a></li>
                            <?php endforeach; ?>
                        </ul>
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
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            <?= lang('stat466.profile.index'); ?>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="<?= base_url('profile/edit') ?>">
                                    <?= lang('stat466.profile.edit'); ?></a></li>
                            <li><a class="dropdown-item" href="<?= base_url('profile/changepw') ?>">
                                    <?= lang('stat466.profile.changepw'); ?></a></li>
                            <li><a class="dropdown-item" href="<?= base_url('logout') ?>">
                                    <?= lang('stat466.profile.logout'); ?></a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container">

        <?php if (isset($breadcrumb) && !is_null($breadcrumb)): ?>
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <?php foreach ($breadcrumb as $crumb): ?>
                        <?php if ($crumb['active'] == true): ?>
                            <li class="breadcrumb-item active" aria-current="page">
                                <?= esc($crumb['title']); ?>
                            </li>
                        <?php else: ?>
                            <li class="breadcrumb-item"><a href="<?= esc($crumb['url']); ?>">
                                    <?= esc($crumb['title']); ?>
                                </a></li>
                        <?php endif; ?>
                    <?php endforeach; ?>

                </ol>
            </nav>
        <?php endif; ?>

        <?php if (isset($message) && !is_null($message)): ?>
            <div class='alert alert-<?= esc($messagetype) ?> mt-2'>
                <?= esc($message); ?>
            </div>
        <?php endif; ?>