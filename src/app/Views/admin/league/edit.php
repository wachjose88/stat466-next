<h1><?= lang('stat466.admin.index') ?></h1>

<div class="card col-md-6">
    <div class="card-header">
        <?= lang('stat466.admin.leagues.edit') ?>
    </div>
    <div class="card-body">
        <form action="<?= base_url('admin/league/edit/') . esc($league['id']) ?>" method="post">
            <?= csrf_field() ?>

            <div class="mb-2">
                <label class="form-label" for="name"><?= lang('stat466.admin.leagues.name') ?>:</label>
                <?php if (isset($validation) && $validation->getError('name')): ?>
                    <div class='alert alert-danger mt-2'>
                        <?= $error = $validation->getError('name'); ?>
                    </div>
                <?php endif; ?>
                <input id="name" type="text" class="form-control" name="name" inputmode="text"
                       placeholder="<?= lang('stat466.admin.leagues.name') ?>"
                       value="<?= esc($league['name']) ?>" required />
            </div>

            <div class="d-grid col-12 col-md-8 mx-auto m-3">
                <button type="submit" class="btn btn-primary btn-block"><?= lang('stat466.admin.save') ?></button>
            </div>
    </div>
</div>