# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminCommentsTbl(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    admin = models.ForeignKey('AdminUsersTbl', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey('UsersTbl', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_comments_tbl'


class AdminUsersTbl(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=110)
    phone_no = models.BigIntegerField()
    login_email = models.CharField(max_length=110)
    access_count = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=110)
    password = models.CharField(max_length=110)
    last_login = models.DateTimeField()
    designation = models.CharField(max_length=110)
    personal_email = models.CharField(max_length=110)
    access = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'admin_users_tbl'


class AdvertisementBannerTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    banner_path = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'advertisement_banner_tbl'


class AppVersionTbl(models.Model):
    android_ver_name = models.CharField(primary_key=True, max_length=10)
    and_is_update = models.IntegerField()
    and_is_force_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_version_tbl'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CoverPicListTbl(models.Model):
    cover_pic_id = models.AutoField(primary_key=True)
    cover_pic = models.CharField(max_length=200)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cover_pic_list_tbl'


class DefaultPlansListTbl(models.Model):
    sr_no = models.AutoField(db_column='sr.no', primary_key=True)  # Field renamed to remove unsuitable characters.
    fantasy_mode_id = models.IntegerField()
    plan_id = models.IntegerField()
    default_plan_status = models.IntegerField()
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_plans_list_tbl'


class DefaultPlayerSettingTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    fantasy_mode_id = models.IntegerField()
    min_batsman = models.IntegerField()
    max_batsman = models.IntegerField()
    min_bowlers = models.IntegerField()
    max_bowlers = models.IntegerField()
    max_player_from_team = models.IntegerField()
    min_allrounder = models.IntegerField(blank=True, null=True)
    max_allrounder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_player_setting_tbl'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FantasyModeTbl(models.Model):
    fantasy_mode_id = models.AutoField(primary_key=True)
    fantasy_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'fantasy_mode_tbl'


class InstalledAppListTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    app_device_id = models.CharField(max_length=45)
    app_os_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'installed_app_list_tbl'


class MasterBankListTbl(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'master_bank_list_tbl'


class MasterPlansListTbl(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_entry_fees = models.IntegerField()
    plan_total_teams = models.IntegerField()
    plan_total_winner = models.IntegerField()
    plan_winner_price = models.DecimalField(max_digits=10, decimal_places=2)
    plan_status = models.IntegerField()
    fantasy_mode_id = models.IntegerField()
    stat_color_code = models.CharField(max_length=20, blank=True, null=True)
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_plans_list_tbl'


class MatchPlansList(models.Model):
    sr_no = models.AutoField(db_column='sr.no', primary_key=True)  # Field renamed to remove unsuitable characters.
    enable_plan_id = models.IntegerField()
    disable_plan_id = models.IntegerField()
    match_id = models.IntegerField()
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_plans_list'


class MatchPlayerDetailTbl(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=45)
    player_key = models.CharField(max_length=20)
    player_role = models.CharField(max_length=45)
    points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    team_key = models.CharField(max_length=45)
    team_name = models.CharField(max_length=45)
    match_id = models.IntegerField()
    batting_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bowling_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fielding_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    player_credit = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_player_detail_tbl'


class MatchScheduleTbl(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_key = models.CharField(max_length=200)
    team_a_name = models.CharField(max_length=45)
    team_a_key = models.CharField(max_length=20)
    team_b_name = models.CharField(max_length=45)
    team_b_key = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    start_time = models.CharField(max_length=45)
    format = models.CharField(max_length=10)
    match_name = models.CharField(max_length=100)
    match_related_name = models.CharField(max_length=70)
    match_short_name = models.CharField(max_length=45)
    season_key = models.CharField(max_length=45)
    season_name = models.CharField(max_length=100)
    match_venue = models.CharField(max_length=200)
    sport_id = models.IntegerField()
    date_created = models.DateTimeField()
    a_1_score = models.CharField(max_length=15, blank=True, null=True)
    b_1_score = models.CharField(max_length=15, blank=True, null=True)
    a_2_score = models.CharField(max_length=15, blank=True, null=True)
    b_2_score = models.CharField(max_length=15, blank=True, null=True)
    a_superover = models.CharField(max_length=15, blank=True, null=True)
    b_superover = models.CharField(max_length=15, blank=True, null=True)
    result_by = models.CharField(max_length=30, blank=True, null=True)
    status_overview = models.CharField(max_length=45, blank=True, null=True)
    final_result = models.CharField(max_length=200, blank=True, null=True)
    is_playerlist_updated = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=45)
    is_featured_match = models.IntegerField()
    a_1_extras = models.IntegerField(blank=True, null=True)
    b_1_extras = models.IntegerField(blank=True, null=True)
    a_2_extras = models.IntegerField(blank=True, null=True)
    b_2_extras = models.IntegerField(blank=True, null=True)
    match_active_inactive_status = models.IntegerField(blank=True, null=True)
    is_abandon = models.IntegerField()
    display_season_name = models.CharField(max_length=100, blank=True, null=True)
    data_review_point = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_schedule_tbl'
        unique_together = (('match_id', 'match_key'),)


class MatchSummaryTbl(models.Model):
    summary_id = models.AutoField(primary_key=True)
    innings = models.CharField(max_length=15)
    player_key = models.CharField(max_length=45)
    player_role = models.CharField(max_length=45)
    runs_scored = models.IntegerField()
    balls = models.IntegerField()
    fours = models.IntegerField()
    sixes = models.IntegerField()
    dot_balls = models.IntegerField()
    strike_rate = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_duckout_except_bowler = models.IntegerField()
    bowling_balls = models.IntegerField()
    economy_rate = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    extras = models.IntegerField()
    maiden_overs = models.IntegerField()
    runs_given_by_bowler = models.IntegerField()
    wickets = models.IntegerField()
    catches = models.IntegerField()
    run_out = models.IntegerField()
    stumps = models.IntegerField()
    helper_catcher = models.IntegerField()
    helper_thrower = models.IntegerField()
    player_id = models.IntegerField()
    in_being_11 = models.IntegerField()
    total_points = models.DecimalField(max_digits=10, decimal_places=0)
    match_id = models.IntegerField()
    batting_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bowling_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fielding_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    player_status = models.CharField(max_length=100, blank=True, null=True)
    player_type = models.CharField(max_length=10, blank=True, null=True)
    team_id = models.CharField(max_length=2, blank=True, null=True)
    bowler_dots = models.IntegerField(blank=True, null=True)
    batting_order = models.IntegerField(blank=True, null=True)
    bowling_order = models.IntegerField(blank=True, null=True)
    team_key = models.CharField(max_length=10, blank=True, null=True)
    team_batting_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_summary_tbl'


class OtpTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_tbl'


class PlayModeTbl(models.Model):
    play_mode_id = models.AutoField(primary_key=True)
    play_mode_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'play_mode_tbl'


class PlayerImageTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    player_key = models.CharField(max_length=50)
    player_name = models.CharField(max_length=50)
    player_pic = models.CharField(max_length=300)
    display_name = models.CharField(max_length=45, blank=True, null=True)
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_image_tbl'


class SportsCategoryTbl(models.Model):
    sport_id = models.AutoField(primary_key=True)
    sport_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'sports_category_tbl'


class StContestPoolTbl(models.Model):
    pool_id = models.AutoField(primary_key=True)
    match_id = models.IntegerField()
    plan_id = models.IntegerField()
    status = models.IntegerField()
    is_cancelled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_contest_pool_tbl'


class StContestTagsTbl(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=45)
    tag_desc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_contest_tags_tbl'


class StDefaultPlansTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    st_plan_id = models.IntegerField(blank=True, null=True)
    default_plan_status = models.IntegerField(blank=True, null=True)
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_default_plans_tbl'


class StMasterPlanTbl(models.Model):
    st_plan_id = models.AutoField(primary_key=True)
    price_pool = models.IntegerField()
    entry_fee = models.IntegerField()
    total_teams = models.IntegerField()
    is_confirm_winnings = models.IntegerField(blank=True, null=True)
    is_multiple_teams = models.IntegerField()
    fantasy_mode_id = models.IntegerField()
    total_winners = models.IntegerField()
    is_repetitive = models.IntegerField()
    rake = models.DecimalField(max_digits=10, decimal_places=0)
    tag_id = models.IntegerField()
    is_active = models.IntegerField(blank=True, null=True)
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)
    is_multiple_winners = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'st_master_plan_tbl'


class StMatchPlanListTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True)
    disable_plan_id = models.IntegerField(blank=True, null=True)
    enable_plan_id = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    after_plan_id = models.IntegerField(blank=True, null=True)
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)
    before_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'st_match_plan_list_tbl'


class StPricePoolBreakupTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    st_plan_id = models.IntegerField()
    start_rank = models.IntegerField()
    end_rank = models.IntegerField()
    rank_amt = models.IntegerField()
    total_rank_amt = models.IntegerField(blank=True, null=True)
    total_rank_users = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_price_pool_breakup_tbl'


class StTeamPlayersTbl(models.Model):
    player_no = models.AutoField(primary_key=True)
    team_id = models.IntegerField()
    player_id = models.IntegerField()
    player_type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'st_team_players_tbl'


class StUserContestDetailTbl(models.Model):
    contest_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    team_id = models.IntegerField()
    pool_id = models.IntegerField()
    total_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField()
    won_amt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_user_contest_detail_tbl'


class StUserTeamsTbl(models.Model):
    team_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    match_id = models.IntegerField()
    user_team_name = models.CharField(max_length=45)
    actual_team_name = models.CharField(max_length=45, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_user_teams_tbl'


class StateListTbl(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'state_list_tbl'


class SuperAdminUser(models.Model):
    sa_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    role = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'super_admin_user'


class TeamFlagTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    team_key = models.CharField(max_length=45)
    team_flag = models.CharField(max_length=500)
    team_name = models.CharField(max_length=45)
    team_color = models.CharField(max_length=20, blank=True, null=True)
    preview_color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_flag_tbl'


class TransactionsTypesTbl(models.Model):
    transaction_type_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    transaction_flag = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'transactions_types_tbl'


class UserAccountDetailTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    bank_acc_no = models.CharField(max_length=45)
    bank_ifsc_code = models.CharField(max_length=45)
    acc_holder_name = models.CharField(max_length=45)
    passbook_cheque_detail = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.IntegerField()
    date_uploaded = models.DateTimeField(blank=True, null=True)
    date_verified = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=45, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    comment_msg = models.CharField(max_length=200, blank=True, null=True)
    bank_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account_detail_tbl'


class UserBonusHistoryTbl(models.Model):
    bonus_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    credit_amount = models.DecimalField(max_digits=10, decimal_places=0)
    date_created = models.DateTimeField()
    plan_id = models.IntegerField(blank=True, null=True)
    debit_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bonus_mode = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bonus_history_tbl'


class UserContestTransaction(models.Model):
    plan_tran_id = models.AutoField(primary_key=True)
    match_id = models.IntegerField()
    plan_id = models.CharField(max_length=45)
    plan_price = models.CharField(max_length=45)
    user_id = models.IntegerField()
    date_created = models.DateTimeField()
    bonus_used = models.DecimalField(max_digits=10, decimal_places=0)
    withdrawable_balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    winning_balance_used = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    unutilized_balance_used = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    contest_id = models.IntegerField(blank=True, null=True)
    fantasy_mode_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_contest_transaction'


class UserFindingTbl(models.Model):
    contest_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    plan_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    contest_code = models.CharField(max_length=45)
    opponent_id = models.IntegerField(blank=True, null=True)
    won_id = models.IntegerField(blank=True, null=True)
    won_amt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_paid = models.IntegerField()
    result_by = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.IntegerField()
    turn_status_id = models.IntegerField(blank=True, null=True)
    play_mode_id = models.CharField(max_length=15)
    fantasy_mode_id = models.IntegerField()
    match_id = models.IntegerField()
    is_contest_cancel = models.IntegerField()
    cancelled_by = models.IntegerField(blank=True, null=True)
    cancelled_date_time = models.DateTimeField(blank=True, null=True)
    contest_created_date = models.DateTimeField(blank=True, null=True)
    opponent_found_date_time = models.DateTimeField(blank=True, null=True)
    won_by_points = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_refund_paid = models.IntegerField(blank=True, null=True)
    is_winning_paid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_finding_tbl'


class UserPanDetailTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    name_on_pan = models.CharField(max_length=45)
    pancard_number = models.CharField(max_length=45)
    dob = models.CharField(max_length=45)
    state_id = models.IntegerField()
    pancard_image = models.CharField(max_length=200, blank=True, null=True)
    date_uploaded = models.DateTimeField(blank=True, null=True)
    date_verified = models.DateTimeField(blank=True, null=True)
    is_verified = models.IntegerField()
    user_id = models.IntegerField()
    comment_msg = models.CharField(max_length=200, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    verified_by_adminname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pan_detail_tbl'


class UserReferralTbl(models.Model):
    referral_id = models.AutoField(primary_key=True)
    sender_id = models.IntegerField()
    receiver_id = models.CharField(max_length=45)
    referral_date = models.DateTimeField()
    referral_code = models.CharField(max_length=45)
    referal_status = models.IntegerField(db_column='referal_Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_referral_tbl'


class UserTransactionHistory(models.Model):
    tr_history_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    deposit_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contest_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    winning_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdrawable_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonus_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)
    transaction_id = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    total_balance_remaining = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contest_id = models.IntegerField(blank=True, null=True)
    withdrawable_status = models.IntegerField(blank=True, null=True)
    refund_amt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    plan_transaction_id = models.IntegerField(blank=True, null=True)
    transaction_code = models.CharField(max_length=20, blank=True, null=True)
    transaction_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_transaction_history'


class UserTransactionTbl(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    gateway_id = models.IntegerField()
    payment_id_from_gateway = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField()
    transaction_amount = models.CharField(max_length=45)
    order_no = models.CharField(max_length=45, blank=True, null=True)
    response = models.CharField(max_length=45, blank=True, null=True)
    gst = models.CharField(max_length=45, blank=True, null=True)
    promotion_id = models.IntegerField(blank=True, null=True)
    transaction_status = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=35, blank=True, null=True)
    payment_mode = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_transaction_tbl'


class UserWalletInfoTbl(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    bonus_balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    winning_balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    unutilized_balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    withdrawable_balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_wallet_info_tbl'


class UsersPlayersTbl(models.Model):
    sl_no = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    contest_id = models.IntegerField()
    player_id = models.IntegerField()
    player_type = models.CharField(max_length=5)
    date_created = models.DateTimeField(blank=True, null=True)
    c_s_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_players_tbl'


class UsersPunam(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_punam'


class UsersTbl(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    user_email = models.CharField(max_length=45)
    user_mobile = models.CharField(max_length=45)
    user_device_id = models.CharField(max_length=500)
    user_login_type = models.CharField(max_length=45)
    user_password = models.CharField(max_length=500, blank=True, null=True)
    user_token = models.CharField(max_length=500)
    user_profile_pic = models.CharField(max_length=200, blank=True, null=True)
    user_gender = models.CharField(max_length=6)
    user_dob = models.CharField(max_length=20, blank=True, null=True)
    user_login_device = models.CharField(max_length=10)
    user_login_from = models.CharField(max_length=45)
    user_date_created = models.DateTimeField()
    user_date_updated = models.DateTimeField(blank=True, null=True)
    user_referral_code = models.CharField(max_length=20, blank=True, null=True)
    user_team_name = models.CharField(max_length=45, blank=True, null=True)
    user_social_media_id = models.CharField(max_length=45, blank=True, null=True)
    is_user_verified = models.IntegerField()
    nic_name = models.CharField(max_length=45, blank=True, null=True)
    ip_adress = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    service_provider = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    device_name = models.CharField(max_length=300, blank=True, null=True)
    os_version = models.CharField(max_length=45, blank=True, null=True)
    cover_pic_id = models.IntegerField(blank=True, null=True)
    is_profile_public = models.IntegerField()
    is_stat_public = models.IntegerField()
    user_city = models.CharField(max_length=25, blank=True, null=True)
    is_email_verified = models.IntegerField(blank=True, null=True)
    is_mob_num_verified = models.IntegerField(blank=True, null=True)
    is_username_updated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_tbl'


class UsersTeamTbl(models.Model):
    team_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    contest_id = models.IntegerField()
    total_points = models.IntegerField(blank=True, null=True)
    team_created_date = models.DateTimeField()
    team_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_team_tbl'


class WalletWithdrawalRequestTbl(models.Model):
    withdrawal_req_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    withdrawal_amt = models.DecimalField(max_digits=10, decimal_places=0)
    request_date = models.DateTimeField()
    is_refunded = models.IntegerField()
    refunded_date = models.DateTimeField(blank=True, null=True)
    withdrawal_transaction_id = models.CharField(max_length=45, blank=True, null=True)
    withdrawal_status = models.IntegerField(blank=True, null=True)
    date_initiated = models.DateTimeField(blank=True, null=True)
    date_successfull = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_withdrawal_request_tbl'


class WithdrawableTransactionsTbl(models.Model):
    credit_transaction_id = models.CharField(max_length=100)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'withdrawable_transactions_tbl'
