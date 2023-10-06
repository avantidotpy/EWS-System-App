float ClassificationTree(floqat* features)
{

    if (features[TotalWorkingYears] <= 1.500000000)
    {

        if (features[MaritalStatus_Single] <= 0.500000000)
        {

            if (features[DistanceFromHome] <= 16.500000000)
            {

                return 0.806451613;
            }
            else
            {

                return 0.250000000;

            }
        }
        else
        {

            if (features[JobRole_Research Scientist] <= 0.500000000)
            {

                return 0.153846154;
            }
            else
            {

                return 0.615384615;

            }

        }
    }
    else
    {

        if (features[OverTime_Yes] <= 0.500000000)
        {

            if (features[WorkLifeBalance] <= 1.500000000)
            {

                return 0.744680851;
            }
            else
            {

                return 0.921438083;

            }
        }
        else
        {

            if (features[MonthlyIncome] <= 3995.000000000)
            {

                return 0.510416667;
            }
            else
            {

                return 0.848039216;

            }

        }

    }
}
