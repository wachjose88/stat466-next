<h1><?= lang('stat466.admin.index') ?></h1>

<div class="card col-md-6">
    <div class="card-header">
        <?= lang('stat466.admin.leagues.users') ?>: <?= esc($league['name']) ?>
    </div>
    <div class="card-body">
        <form action="<?= base_url('admin/league/') . esc($league['id']) ?>/users" method="post">
            <?= csrf_field() ?>

            <div class="mb-2">
                <?php if (isset($validation) && $validation->getError('usersofleague')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('usersofleague'); ?>
                    </div>
                <?php endif; ?>
                <select id="usersofleague" name="usersofleague[]" class="form-select" multiple
                        aria-label="multiple select groups">
                    <?php foreach ($users as $key => $user): ?>
                    <option value="<?= esc($user->id) ?>"
                    <?php if (array_key_exists($user->id, $usersofleague)) echo 'selected'; ?>
                    ><?= esc($user->first_name) ?> <?= esc($user->last_name) ?></option>
                    <?php endforeach; ?>
                </select>
            </div>

            <div class="d-grid col-12 col-md-8 mx-auto m-3">
                <button type="submit" class="btn btn-primary btn-block"><?= lang('stat466.admin.save') ?></button>
            </div>
    </div>
</div>