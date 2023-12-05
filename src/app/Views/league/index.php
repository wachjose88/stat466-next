<h1>
    <?= lang('stat466.leagues.index') ?>:
    <?= esc($league['name']) ?>
</h1>

<h3>
    <?= lang('stat466.leagues.users') ?>
</h3>

<?php if (count($league['users']) > 0): ?>
<div class="card-group">
    <?php foreach ($league['users'] as $user): ?>
        <div class="card border-primary">
            <div class="card-header text-bg-success">
                <h5 class="card-title">
                    <?= esc($user['profile']->first_name); ?>
                    <?= esc($user['profile']->last_name); ?>
                </h5>
            </div>
            <div class="card-body">
                TODO
            </div>
        </div>
    <?php endforeach; ?>
</div>
<?php endif; ?>

<h3>
    <?= lang('stat466.leagues.result_2p') ?>
</h3>
<ul>
    <li>
        <a href="<?= base_url("league/$league_id/create/result2p"); ?>">
            <?= lang('stat466.leagues.create_result_2p') ?>
    </li>
</ul>