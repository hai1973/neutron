# Copyright 2018 NOKIA
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from alembic import op
import sqlalchemy as sa

"""add security group stateful

Revision ID: 18a7e90ae768
Revises: 2217c4222de6
Create Date: 2018-04-26 14:44:52.635576

"""

# revision identifiers, used by Alembic.
revision = '18a7e90ae768'
down_revision = '2217c4222de6'


def upgrade():
    op.add_column('securitygroups',
                  sa.Column('stateful',
                            sa.Boolean(),
                            server_default=sa.sql.true(),
                            nullable=False))
