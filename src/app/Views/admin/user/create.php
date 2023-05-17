<h1><?= lang('stat466.admin.index') ?></h1>

<div class="card col-md-6">
    <div class="card-header">
        <?= lang('stat466.admin.users.create') ?>
    </div>
    <div class="card-body">
        <form action="<?= base_url('admin/user/create') ?>" method="post">
            <?= csrf_field() ?>

            <div class="mb-2">
                <label class="form-label" for="username"><?= lang('stat466.admin.users.username') ?>:</label>
                <?php if (isset($validation) && $validation->getError('username')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('username'); ?>
                    </div>
                <?php endif; ?>
                <input id="username" type="text" class="form-control" name="username" inputmode="text"
                       placeholder="<?= lang('stat466.admin.users.username') ?>"
                       value="<?= $old['username'] ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="password"><?= lang('stat466.admin.users.password') ?>:</label>
                <?php if (isset($validation) && $validation->getError('password')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('password'); ?>
                    </div>
                <?php endif; ?>
                <input id="password" type="password" class="form-control" name="password" inputmode="text"
                       placeholder="<?= lang('stat466.admin.users.password') ?>"
                       value="" />
            </div>

            <div class="mb-2">
                <label class="form-label" for="email"><?= lang('stat466.admin.users.email') ?>:</label>
                <?php if (isset($validation) && $validation->getError('email')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('email'); ?>
                    </div>
                <?php endif; ?>
                <input id="email" type="email" class="form-control" name="email" inputmode="text"
                       placeholder="<?= lang('stat466.admin.users.email') ?>"
                       value="<?= $old['email'] ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="first_name"><?= lang('stat466.admin.users.first_name') ?>:</label>
                <?php if (isset($validation) && $validation->getError('first_name')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('first_name'); ?>
                    </div>
                <?php endif; ?>
                <input id="first_name" type="text" class="form-control" name="first_name" inputmode="text"
                       placeholder="<?= lang('stat466.admin.users.first_name') ?>"
                       value="<?= $old['first_name'] ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="last_name"><?= lang('stat466.admin.users.last_name') ?>:</label>
                <?php if (isset($validation) && $validation->getError('last_name')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('last_name'); ?>
                    </div>
                <?php endif; ?>
                <input id="last_name" type="text" class="form-control" name="last_name" inputmode="text"
                       placeholder="<?= lang('stat466.admin.users.last_name') ?>"
                       value="<?= $old['last_name'] ?>" required />
            </div>

            <div class="mb-2">
                <label class="form-label" for="groups"><?= lang('stat466.admin.users.groups') ?>:</label>
                <?php if (isset($validation) && $validation->getError('groups')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('groups'); ?>
                    </div>
                <?php endif; ?>
                <select id="groups" name="groups[]" class="form-select" multiple aria-label="multiple select groups">
                    <?php foreach ($groups as $key => $group): ?>
                    <option value="<?= esc($key) ?>"
                    <?php if (in_array($key, $old['groups'])) echo 'selected'; ?>
                    ><?= esc($group['title']) ?></option>
                    <?php endforeach; ?>
                </select>
            </div>


            <div class="mb-2">
                <?php if (isset($validation) && $validation->getError('active')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('active'); ?>
                    </div>
                <?php endif; ?>
                <input id="active" type="checkbox" class="form-check-input" name="active" value="1"
                      <?php if ($old['active'] == '1') echo 'checked' ?> />
                <label class="form-check-label" for="active"><?= lang('stat466.admin.users.active') ?>:</label>
            </div>

            <div class="d-grid col-12 col-md-8 mx-auto m-3">
                <button type="submit" class="btn btn-primary btn-block"><?= lang('stat466.admin.save') ?></button>
            </div>
    </div>
</div>