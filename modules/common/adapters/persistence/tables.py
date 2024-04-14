import sqlalchemy as sa


metadata = sa.MetaData()


network_traffic_table = sa.Table(
    "network_traffic",
    metadata,
    sa.Column("id", sa.BigInteger, primary_key=True),
    sa.Column("timestamp", sa.String(50)),
    sa.Column("source_ip", sa.String(50)),
    sa.Column("destination_ip", sa.String(50)),
    sa.Column("protocol", sa.String(50)),
    sa.Column("port", sa.String(50)),
    sa.Column("packet_size", sa.String(50)),
    sa.Column("prediction", sa.String(50)),
)


mail_table = sa.Table(
    "mail",
    metadata,
    sa.Column("mail_id", sa.BigInteger, primary_key=True),
    sa.Column("mail", sa.String(50), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
)
