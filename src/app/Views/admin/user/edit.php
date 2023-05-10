<h1><?= lang('stat466.admin.index') ?></h1>

<div class="card col-md-6">
    <div class="card-header">
        <?= lang('stat466.admin.users.edit') ?>
    </div>
    <div class="card-body">
        <form action="<?= base_url('admin/user/edit/') . esc($user->id) ?>" method="post">
            <?= csrf_field() ?>

            <div class="mb-2">
                <label class="form-label" for="username"><?= lang('stat466.admin.users.username') ?>:</label>
                <?php if (isset($validation) && $validation->getError('username')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('username'); ?>
                    </div>
                <?php endif; ?>
                <input type="username" class="form-control" name="username" inputmode="text"
                       placeholder="<?= lang('stat466.admin.users.username') ?>"
                       value="<?= esc($user->username) ?>" required />
            </div>

            <div class="d-grid col-12 col-md-8 mx-auto m-3">
                <button type="submit" class="btn btn-primary btn-block"><?= lang('stat466.admin.save') ?></button>
            </div>
    </div>
</div>