import sqlalchemy as sa


metadata = sa.MetaData()


network_traffic_table = sa.Table(
    "network_traffic",
    metadata,
    sa.Column("id", sa.BigInteger, primary_key=True),
    sa.Column("duration", sa.String(50)),
    sa.Column("protocol_type", sa.String(50)),
    sa.Column("service", sa.String(50)),
    sa.Column("flag", sa.String(50)),
    sa.Column("src_bytes", sa.String(50)),
    sa.Column("dst_bytes", sa.String(50)),
    sa.Column("land", sa.String(50)),
    sa.Column("wrong_fragment", sa.String(50)),
    sa.Column("urgent", sa.String(50)),
    sa.Column("hot", sa.String(50)),
    sa.Column("num_failed_logins", sa.String(50)),
    sa.Column("logged_in", sa.String(50)),
    sa.Column("num_compromised", sa.String(50)),
    sa.Column("root_shell", sa.String(50)),
    sa.Column("su_attempted", sa.String(50)),
    sa.Column("num_root", sa.String(50)),
    sa.Column("num_file_creations", sa.String(50)),
    sa.Column("num_shells", sa.String(50)),
    sa.Column("num_access_files", sa.String(50)),
    sa.Column("num_outbound_cmds", sa.String(50)),
    sa.Column("is_host_login", sa.String(50)),
    sa.Column("is_guest_login", sa.String(50)),
    sa.Column("count", sa.String(50)),
    sa.Column("srv_count", sa.String(50)),
    sa.Column("serror_rate", sa.String(50)),
    sa.Column("srv_serror_rate", sa.String(50)),
    sa.Column("rerror_rate", sa.String(50)),
    sa.Column("srv_rerror_rate", sa.String(50)),
    sa.Column("same_srv_rate", sa.String(50)),
    sa.Column("diff_srv_rate", sa.String(50)),
    sa.Column("srv_diff_host_rate", sa.String(50)),
    sa.Column("dst_host_count", sa.String(50)),
    sa.Column("dst_host_srv_count", sa.String(50)),
    sa.Column("dst_host_same_srv_rate", sa.String(50)),
    sa.Column("dst_host_diff_srv_rate", sa.String(50)),
    sa.Column("dst_host_same_src_port_rate", sa.String(50)),
    sa.Column("dst_host_srv_diff_host_rate", sa.String(50)),
    sa.Column("dst_host_serror_rate", sa.String(50)),
    sa.Column("dst_host_srv_serror_rate", sa.String(50)),
    sa.Column("dst_host_rerror_rate", sa.String(50)),
    sa.Column("dst_host_srv_rerror_rate", sa.String(50)),
    sa.Column("label", sa.String(50)),
    sa.Column("difficulty", sa.String(50)),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
)


mail_table = sa.Table(
    "mail",
    metadata,
    sa.Column("mail_id", sa.BigInteger, primary_key=True),
    sa.Column("mail", sa.String(50)),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
)
