def DynamicRuleGenerator(feature):

    if feature[TotalWorkingYears] <= 1.500000000:
    
        visited.append(TotalWorkingYears)

        if feature[MaritalStatus_Single] <= 0.500000000:
        
            visited.append(MaritalStatus_Single)

            if feature[DistanceFromHome] <= 16.500000000:
            
                visited.append(DistanceFromHome)

                if feature[BusinessTravel_Travel_Frequently] <= 0.500000000:
                
                    visited.append(BusinessTravel_Travel_Frequently)

                    if feature[JobSatisfaction] <= 1.500000000:
                    
                        visited.append(JobSatisfaction)

                        return 0.500000000
                    
                    else:
                    

                        return 1.000000000

                
                else:
                

                    if feature[HourlyRate] <= 43.500000000:
                    
                        visited.append(HourlyRate)

                        return 1.000000000
                    
                    else:
                    

                        return 0.000000000

                    

                
            
            else:
            

                if feature[PercentSalaryHike] <= 20.500000000:
                
                    visited.append(PercentSalaryHike)

                    return 0
                
                else:
            
                    return 1
                

            
        
        else:
        

            if feature[JobRole_ResearchScientist] <= 0.500000000:
            
                visited.append(JobRole_ResearchScientist)

                if feature[EducationField_Medical] <= 0.500000000:
                
                    visited.append(EducationField_Medical)

                    if feature[BusinessTravel_Non-Travel] <= 0.500000000:
                    
                        visited.append(BusinessTravel_Non-Travel)

                        return 0.000000000
                    
                    else:
                    

                        return 1.000000000

                    
                
                else:
                

                    if feature[Gender_Male] <= 0.500000000:
                    
                        visited.append(Gender_Male)

                        return 0.750000000
                    
                    else:
                    

                        return 0.000000000

                    

                
            
            else:
            

                if feature[MonthlyRate] <= 22161.500000000:
                
                    visited.append(MonthlyRate)

                    if feature[RelationshipSatisfaction] <= 1.500000000:
                    
                        visited.append(RelationshipSatisfaction)

                        return 0.000000000
                    
                    else:
                    

                        return 1.000000000

                    
                
                else:
                

                    return 0.000000000

                

            

        
    
    else:
    

        if feature[OverTime_No] <= 0.500000000:
        
            visited.append(OverTime_No)

            if feature[MonthlyIncome] <= 3995.000000000:
            
                visited.append(MonthlyIncome)

                if feature[StockOptionLevel] <= 0.500000000:
                
                    visited.append(StockOptionLevel)

                    if feature[DistanceFromHome] <= 5.500000000:
                    
                        visited.append(DistanceFromHome)

                        return 0.521739130
                    
                    else:
                    

                        return 0.157894737

                    
                
                else:
                

                    if feature[Age] <= 26.500000000:
                    
                        visited.append(Age)

                        return 0.142857143
                    
                    else:
                    

                        return 0.702127660

                    

                
            
            else:
            

                if feature[MaritalStatus_Single] <= 0.500000000:
                
                    visited.append(MaritalStatus_Single)

                    if feature[MonthlyIncome] <= 19853.000000000:
                    
                        visited.append(MonthlyIncome)

                        return 0.931506849
                    
                    else:
                    

                        return 0.000000000

                    
                
                else:
                

                    if feature[JobRole_SalesExecutive] <= 0.500000000:
                    
                        visited.append(JobRole_SalesExecutive)

                        return 0.862068966
                    
                    else:
                    

                        return 0.428571429

                    

                

            
        
        else:
        

            if feature[WorkLifeBalance] <= 1.500000000:
            
                visited.append(WorkLifeBalance)

                if feature[DailyRate] <= 1146.000000000:
                
                    visited.append(DailyRate)

                    if feature[JobInvolvement] <= 2.500000000:
                    
                        visited.append(JobInvolvement)

                        return 0.300000000
                    
                    else:
                    

                        return 0.782608696

                    
                
                else:
                

                    return 1.000000000

                
            
            else:
            

                if feature[YearsAtCompany] <= 38.500000000:
                
                    visited.append(YearsAtCompany)

                    if feature[YearsAtCompany] <= 4.500000000:
                    
                        visited.append(YearsAtCompany)

                        return 0.875486381
                    
                    else:
                    

                        return 0.947261663

                    
                
                else:
                

                    return 0.000000000

                

            

        

    
