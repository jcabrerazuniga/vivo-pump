#!/usr/bin/env/python

"""
    make_enum.py -- make enumerations for grants
"""

from datetime import datetime

from pump.vivopump import get_parms, create_enum

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2016 (c) Michael Conlon"
__license__ = "BSD 3-Clause license"
__version__ = "0.1.1"


def main():
    """
    Generate the enums for grants
    """
    print(datetime.now(), "Start")
    parms = get_parms()

    #   person via Orcid

    query = """
    SELECT (MIN (?xshort) AS ?short) ?vivo
    WHERE
    {
          ?vivo vivo:orcidId ?xshort .
    }
    GROUP BY ?vivo
    ORDER BY ?short
    """

    create_enum("orcid_enum.txt", query, parms)

    #   department via label

    query = """
    SELECT (MIN (?xlabel) AS ?short) ?vivo
    WHERE
    {
          {?vivo a vivo:Department . } UNION {?vivo a vivo:Institute . } UNION {?vivo a vivo:School . }
          UNION {?vivo a vivo:Center .} UNION {?vivo a vivo:College . }
          ?vivo rdfs:label ?xlabel .
    }
    GROUP BY ?vivo
    ORDER BY ?short
    """

    create_enum("dept_enum.txt", query, parms)

    #   Funding Organizations via label

    query = """
    SELECT (MIN (?xlabel) AS ?short) ?vivo
    WHERE
    {
          ?vivo a vivo:FundingOrganization .
          ?vivo rdfs:label ?xlabel .
    }
    GROUP BY ?vivo
    ORDER BY ?short
    """

    create_enum("sponsor_enum.txt", query, parms)

    #   Concept via label

    query = """
    SELECT (MIN (?xlabel) AS ?short) ?vivo
    WHERE
    {
          ?vivo a skos:Concept .
          ?vivo rdfs:label ?xlabel .
    }
    GROUP BY ?vivo
    ORDER BY ?short
    """

    create_enum("concept_enum.txt", query, parms)

    #   dates via datetime

    query = """
    SELECT ?short ?vivo
    WHERE
    {
          ?vivo a vivo:DateTimeValue .
#          ?vivo vivo:dateTimePrecision vivo:yearMonthDayPrecision .
          ?vivo vivo:dateTime ?short .
    }
    ORDER BY ?short
    """

    create_enum("date_enum.txt", query, parms, trim=10)

    print(datetime.now(), "End")

if __name__ == "__main__":
    main()
