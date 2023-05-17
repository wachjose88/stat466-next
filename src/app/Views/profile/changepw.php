<h1><?= lang('stat466.profile.index') ?></h1>

<div class="card col-md-6">
    <div class="card-header">
        <?= lang('stat466.profile.changepw') ?>
    </div>
    <div class="card-body">
        <form action="<?= base_url('profile/changepw') ?>" method="post">
            <?= csrf_field() ?>

            <div class="mb-2">
                <label class="form-label" for="oldpassword"><?= lang('stat466.profile.oldpassword') ?>:</label>
                <?php if (isset($validation) && $validation->getError('oldpassword')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('oldpassword'); ?>
                    </div>
                <?php endif; ?>
                <input id="oldpassword" type="password" class="form-control" name="oldpassword" inputmode="text"
                       placeholder="<?= lang('stat466.profile.oldpassword') ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="newpassword"><?= lang('stat466.profile.newpassword') ?>:</label>
                <?php if (isset($validation) && $validation->getError('newpassword')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('newpassword'); ?>
                    </div>
                <?php endif; ?>
                <input id="newpassword" type="password" class="form-control" name="newpassword" inputmode="text"
                       placeholder="<?= lang('stat466.profile.newpassword') ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="confirmpassword"><?= lang('stat466.profile.confirmpassword') ?>:</label>
                <?php if (isset($validation) && $validation->getError('confirmpassword')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('confirmpassword'); ?>
                    </div>
                <?php endif; ?>
                <input id="confirmpassword" type="password" class="form-control" name="confirmpassword" inputmode="text"
                       placeholder="<?= lang('stat466.profile.confirmpassword') ?>" required />
            </div>

            <div class="d-grid col-12 col-md-8 mx-auto m-3">
                <button type="submit" class="btn btn-primary btn-block"><?= lang('stat466.profile.changepw') ?></button>
            </div>
    </div>
</div>