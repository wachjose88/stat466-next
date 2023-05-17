<h1><?= lang('stat466.admin.index') ?></h1>

<div class="card">
    <div class="card-header">
        <?= lang('stat466.admin.users.users') ?>
    </div>
    <div class="card-body">
        <ul>
            <li>
                <a href="<?= base_url('admin/user/create') ?>">
                    <?= lang('stat466.admin.users.create') ?></a>
            </li>
        </ul>
        <table class="table">
            <thead>
                <tr>
                    <th><?= lang('stat466.admin.users.username') ?></th>
                    <th><?= lang('stat466.admin.users.name') ?></th>
                    <th><?= lang('stat466.admin.users.email') ?></th>
                    <th><?= lang('stat466.admin.users.groups') ?></th>
                    <th><?= lang('stat466.admin.users.active') ?></th>
                    <th><?= lang('stat466.admin.users.actions') ?></th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($users as $user): ?>
                    <tr>
                        <td>
                            <a href="<?= base_url('admin/user/edit/') . esc($user->id); ?>">
                                <?= esc($user->username) ?>
                            </a>
                        </td>
                        <td><?= esc($user->first_name) . ' ' . esc($user->last_name) ?></td>
                        <td><?= esc($user->email) ?></td>
                        <td><?= implode(', ', $user->getGroups()) ?></td>
                        <td>
                            <?php if ($user->active): ?>
                            X
                            <?php endif; ?>
                        </td>
                        <td>
                            <a href="<?= base_url('admin/user/edit/') . esc($user->id); ?>">
                                <?= lang('stat466.admin.users.editaction') ?></a>,
                            <a href="<?= base_url('admin/user/delete/') . esc($user->id); ?>"
                               onclick="return confirm('<?= lang('stat466.admin.users.deleteconfirm') ?>')">
                                <?= lang('stat466.admin.users.deleteaction') ?></a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</div>