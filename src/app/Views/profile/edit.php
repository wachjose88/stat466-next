<h1><?= lang('stat466.profile.index') ?></h1>

<div class="card col-md-6">
    <div class="card-header">
        <?= lang('stat466.profile.edit') ?>
    </div>
    <div class="card-body">
        <form action="<?= base_url('profile/edit') ?>" method="post">
            <?= csrf_field() ?>

            <div class="mb-2">
                <label class="form-label" for="username"><?= lang('stat466.profile.username') ?>:</label>
                <?php if (isset($validation) && $validation->getError('username')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('username'); ?>
                    </div>
                <?php endif; ?>
                <input id="username" type="text" class="form-control" name="username" inputmode="text"
                       placeholder="<?= lang('stat466.profile.username') ?>"
                       value="<?= esc($user->username) ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="email"><?= lang('stat466.profile.email') ?>:</label>
                <?php if (isset($validation) && $validation->getError('email')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('email'); ?>
                    </div>
                <?php endif; ?>
                <input id="email" type="email" class="form-control" name="email" inputmode="text"
                       placeholder="<?= lang('stat466.profile.email') ?>"
                       value="<?= esc($user->email) ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="first_name"><?= lang('stat466.profile.first_name') ?>:</label>
                <?php if (isset($validation) && $validation->getError('first_name')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('first_name'); ?>
                    </div>
                <?php endif; ?>
                <input id="first_name" type="text" class="form-control" name="first_name" inputmode="text"
                       placeholder="<?= lang('stat466.profile.first_name') ?>"
                       value="<?= esc($user->first_name) ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="last_name"><?= lang('stat466.profile.last_name') ?>:</label>
                <?php if (isset($validation) && $validation->getError('last_name')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('last_name'); ?>
                    </div>
                <?php endif; ?>
                <input id="last_name" type="text" class="form-control" name="last_name" inputmode="text"
                       placeholder="<?= lang('stat466.profile.last_name') ?>"
                       value="<?= esc($user->last_name) ?>" required />
            </div>

            <div class="d-grid col-12 col-md-8 mx-auto m-3">
                <button type="submit" class="btn btn-primary btn-block"><?= lang('stat466.profile.save') ?></button>
            </div>
    </div>
</div>