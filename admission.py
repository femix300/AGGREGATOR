#!/usr/bin/python3
from SA_version.varsity import University
from SA_version.schools import Faculty
from SA_version.sa_data_base.ukzn_data_base import ukzn_data
from SA_version.sa_data_base.up_data_base import up_data
from SA_version.sa_data_base.wits_data_base import wits_data
from SA_version.sa_data_base.uct_data_base import uct_data
from SA_version.sa_data_base.us_data_base import us_data
from SA_version.sa_data_base.uj_data_base import uj_data


data_base = [ukzn_data,
        up_data,
        wits_data,
        uct_data,
        us_data,
        uj_data]

University.admission(data_base)
