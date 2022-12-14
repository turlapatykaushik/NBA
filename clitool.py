# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 15:22:16 2022

@author: kaushik
"""

from nba_api.stats.endpoints import alltimeleadersgrids
from nba_api.stats.endpoints import franchiseleaders
from nba_api.stats.endpoints import leagueleaders

from nba_api.stats.endpoints import teamhistoricalleaders
from nba_api.stats.library.parameters import *
from nba_api.stats.static import *

print("Welcome to the NBA stats tool\n")

print("Please select one of the two choices from below")
#print("1. League Wide Stats  2. Team Stats")
user_choice = int(input("1.All-time Stats  2.Season-wise stats \n"))
if(user_choice == 1) or (user_choice == 2):
    user_choice_two = int(input("1.League-wide stats 2.Team stats \n"))
else:
    input("Invalid choice. Press ctrl+C to kill the program and try again")

    
if(user_choice ==1) and(user_choice_two == 1):
    user_choice_three = int(input("1. Points 2. Assists 3.Rebounds 4. Steals 5. Blocks \n"))
    alltimeleadersgrids = alltimeleadersgrids.AllTimeLeadersGrids(league_id =LeagueID.default,per_mode_simple=PerModeSimple.default,season_type=SeasonType.default,topx=1)
    alltimeleadersgrids_dict = alltimeleadersgrids.get_normalized_dict()
   
    if (user_choice_three == 1):
        print("Player Name: ", alltimeleadersgrids_dict['PTSLeaders'][0]['PLAYER_NAME'])
        print("Points: ", alltimeleadersgrids_dict['PTSLeaders'][0]['PTS'])
    elif(user_choice_three == 2):
        print("Player Name: ", alltimeleadersgrids_dict['ASTLeaders'][0]['PLAYER_NAME'])
        print("Assists: ", alltimeleadersgrids_dict['ASTLeaders'][0]['AST'])       
    elif(user_choice_three == 3):
        print("Player Name: ", alltimeleadersgrids_dict['REBLeaders'][0]['PLAYER_NAME'])
        print("Rebounds: ", alltimeleadersgrids_dict['REBLeaders'][0]['REB'])
    
    elif(user_choice_three == 4):
        print("Player Name: ", alltimeleadersgrids_dict['STLLeaders'][0]['PLAYER_NAME'])
        print("Steals: ", alltimeleadersgrids_dict['STLLeaders'][0]['STL'])
    
    elif(user_choice_three == 5):
        print("Player Name: ", alltimeleadersgrids_dict['BLKLeaders'][0]['PLAYER_NAME'])
        print("Blocks: ", alltimeleadersgrids_dict['BLKLeaders'][0]['BLK'])
        
elif(user_choice ==1) and(user_choice_two == 2):
    nba_teams = teams.get_teams()
    #print(nba_teams)
    user_choice_four = input("Enter the team code \n")
    for team in nba_teams:
        if(team['abbreviation']==user_choice_four):
            franchiseleaders = franchiseleaders.FranchiseLeaders(team_id = team['id'],league_id_nullable = LeagueID.default)
            franchiseleaders_dict = franchiseleaders.get_normalized_dict()
            #print(franchiseleaders_dict)
            user_choice_three = int(input("1. Points 2. Assists 3.Rebounds 4. Steals 5. Blocks \n"))
            if (user_choice_three == 1):
                print("Player Name: ", franchiseleaders_dict['FranchiseLeaders'][0]['PTS_PLAYER'])
                print("Points: ", franchiseleaders_dict['FranchiseLeaders'][0]['PTS'])  
            elif(user_choice_three == 2):
                print("Player Name: ", franchiseleaders_dict['FranchiseLeaders'][0]['AST_PLAYER'])
                print("Assists: ", franchiseleaders_dict['FranchiseLeaders'][0]['AST'])  
            elif(user_choice_three == 3):
                print("Player Name: ", franchiseleaders_dict['FranchiseLeaders'][0]['REB_PLAYER'])
                print("Rebounds: ", franchiseleaders_dict['FranchiseLeaders'][0]['REB'])      
            elif(user_choice_three == 4):
                print("Player Name: ", franchiseleaders_dict['FranchiseLeaders'][0]['STL_PLAYER'])
                print("Steals: ", franchiseleaders_dict['FranchiseLeaders'][0]['STL'])           
            elif(user_choice_three == 5):
                print("Player Name: ", franchiseleaders_dict['FranchiseLeaders'][0]['BLK_PLAYER'])
                print("Blocks: ", franchiseleaders_dict['FranchiseLeaders'][0]['BLK'])  
        else:
            continue
        
elif(user_choice ==2) and(user_choice_two == 1):
    user_choice_four = input("Enter the season e.g. 2020-21, 2019-20, 2016-17, etc., \n")
    user_choice_three = int(input("1. Points 2. Assists 3.Rebounds 4. Steals 5. Blocks \n"))
    if(user_choice_three == 1):
        leagueleaders = leagueleaders.LeagueLeaders(league_id =LeagueID.default,per_mode48=PerMode48.default,scope=Scope.default,season=user_choice_four,season_type_all_star=SeasonType.default,stat_category_abbreviation='PTS')
        leagueleaders_dict = leagueleaders.get_normalized_dict()
        print("Player Name: ", leagueleaders_dict['LeagueLeaders'][0]['PLAYER'])
        print("Points: ", leagueleaders_dict['LeagueLeaders'][0]['PTS'])
    elif(user_choice_three == 2):
        leagueleaders = leagueleaders.LeagueLeaders(league_id =LeagueID.default,per_mode48=PerMode48.default,scope=Scope.default,season=user_choice_four,season_type_all_star=SeasonType.default,stat_category_abbreviation='AST')
        leagueleaders_dict = leagueleaders.get_normalized_dict()
        print("Player Name: ", leagueleaders_dict['LeagueLeaders'][0]['PLAYER'])
        print("Assists: ", leagueleaders_dict['LeagueLeaders'][0]['AST'])
    elif(user_choice_three == 3):
        leagueleaders = leagueleaders.LeagueLeaders(league_id =LeagueID.default,per_mode48=PerMode48.default,scope=Scope.default,season=user_choice_four,season_type_all_star=SeasonType.default,stat_category_abbreviation='REB')
        leagueleaders_dict = leagueleaders.get_normalized_dict()
        print("Player Name: ", leagueleaders_dict['LeagueLeaders'][0]['PLAYER'])
        print("Rebounds: ", leagueleaders_dict['LeagueLeaders'][0]['REB'])  
    elif(user_choice_three == 4):
        leagueleaders = leagueleaders.LeagueLeaders(league_id =LeagueID.default,per_mode48=PerMode48.default,scope=Scope.default,season=user_choice_four,season_type_all_star=SeasonType.default,stat_category_abbreviation='STL')
        leagueleaders_dict = leagueleaders.get_normalized_dict()
        print("Player Name: ", leagueleaders_dict['LeagueLeaders'][0]['PLAYER'])
        print("Steals: ", leagueleaders_dict['LeagueLeaders'][0]['STL'])
    elif(user_choice_three == 5):
        leagueleaders = leagueleaders.LeagueLeaders(league_id =LeagueID.default,per_mode48=PerMode48.default,scope=Scope.default,season=user_choice_four,season_type_all_star=SeasonType.default,stat_category_abbreviation='BLK')
        leagueleaders_dict = leagueleaders.get_normalized_dict()
        print("Player Name: ", leagueleaders_dict['LeagueLeaders'][0]['PLAYER'])
        print("Blocks: ", leagueleaders_dict['LeagueLeaders'][0]['BLK']) 
