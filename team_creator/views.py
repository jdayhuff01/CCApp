from django.shortcuts import render
from django.db.models import F
from team_creator.forms import TeamsForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import GameRosters
from django.http import HttpResponseRedirect
from django.http import HttpResponse



game = GameRosters.objects.get(id=1)

team1_players  = [game.p1_team1,game.p2_team1,game.p3_team1,game.p4_team1,game.p5_team1,game.p6_team1]
team2_players  = [game.p1_team2,game.p2_team2,game.p3_team2,game.p4_team2,game.p5_team2,game.p6_team2]

currentTurn = 1
shotsMadeTurn = [0,0,0,0,0,0]
currentOrder = [1,1,1,1,1,1]
shotsTakenTurn = 0

# Create your views here.

def team_view(request):
    gameRoster = GameRosters.objects.all()
    post = GameRosters.objects.get(id=1)
    shooterName = post.p1_team1
    context = {
        'gameRoster': gameRoster,
        'shooterName': shooterName

    }
    return render(request, 'team_view.html', context)

@csrf_exempt
def team_players(request):
    if request.POST:
        instance = GameRosters.objects.get(pk=1)
        form = TeamsForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
            
        return redirect(team_view)
    return render(request, "team_players.html", {'form1': TeamsForm})


def shotForm(request, pk):
    
   
    post = GameRosters.objects.get(id=1)

    global shotsTakenTurn, shotsMadeTurn, currentTurn, currentOrder

    numOfShooters = sum(currentOrder)

    
    player = [i for i, n in enumerate(currentOrder) if n == 1][shotsTakenTurn]
    
    
    if currentTurn == 1:
        if player == 0 and currentOrder[0] == 1:
            if pk == 1:
                post.p11_makes += 1
                post.team2_cups -= 1
                shotsMadeTurn[0] = 1
                post.save()
            if pk == 0:
                post.p11_misses += 1
                shotsMadeTurn[0] = 0
                post.save()
           
        if player == 1 and currentOrder[1] == 1:
            if pk == 1:
                post.p21_makes += 1
                post.team2_cups -= 1
                shotsMadeTurn[1] = 1
                post.save()
            if pk == 0:
                post.p21_misses += 1
                shotsMadeTurn[1] = 0
                post.save()
            
        if player == 2 and currentOrder[2] == 1:
            if pk == 1:
                post.p31_makes += 1
                post.team2_cups -= 1
                shotsMadeTurn[2] = 1
                post.save()
            if pk == 0:
                post.p31_misses += 1
                shotsMadeTurn[2] = 0
                post.save()
            
        if player == 3 and currentOrder[3] == 1:
            if pk == 1:
                post.p41_makes += 1
                post.team2_cups -= 1
                shotsMadeTurn[3] = 1
                post.save()
            if pk == 0:
                post.p41_misses += 1
                shotsMadeTurn[3] = 0
                post.save()
            
        if player == 4 and currentOrder[4] == 1:
            if pk == 1:
                post.p51_makes += 1
                post.team2_cups -= 1
                shotsMadeTurn[4] = 1
                post.save()
            if pk == 0:
                post.p51_misses += 1
                shotsMadeTurn[4] = 0
                post.save()
            
        if player == 5 and currentOrder[5] == 1:
            if pk == 1:
                post.p61_makes += 1
                post.team2_cups -= 1
                shotsMadeTurn[5] = 1
                post.save()
            if pk == 0:
                post.p61_misses += 1
                shotsMadeTurn[5] = 0
                post.save()
        shotsTakenTurn += 1
        
        #End of round
        if shotsTakenTurn == numOfShooters:
            shotsTakenTurn = 0
            currentOrder = shotsMadeTurn

            #End of Turn
            if sum(shotsMadeTurn) < 2:
                currentTurn = 2
                currentOrder = [1,1,1,1,1,1]
            shotsMadeTurn = [0,0,0,0,0,0]
        


    elif currentTurn == 2:
        if player == 0 and currentOrder[0] == 1:
            if pk == 1:
                post.p12_makes += 1
                post.team1_cups -= 1
                shotsMadeTurn[0] = 1
                post.save()
            if pk == 0:
                post.p12_misses += 1
                shotsMadeTurn[0] = 0
                post.save()
            
        if player == 1 and currentOrder[1] == 1:
            if pk == 1:
                post.p22_makes += 1
                post.team1_cups -= 1
                shotsMadeTurn[1] = 1
                post.save()
            if pk == 0:
                post.p22_misses += 1
                shotsMadeTurn[1] = 0
                post.save()
            
        if player == 2 and currentOrder[2] == 1:
            if pk == 1:
                post.p32_makes += 1
                post.team1_cups -= 1
                shotsMadeTurn[2] = 1
                post.save()
            if pk == 0:
                post.p32_misses += 1
                shotsMadeTurn[2] = 0
                post.save()
            
        if player == 3 and currentOrder[3] == 1:
            if pk == 1:
                post.p42_makes += 1
                post.team1_cups -= 1
                shotsMadeTurn[3] = 1
                post.save()
            if pk == 0:
                post.p42_misses += 1
                shotsMadeTurn[3] = 0
                post.save()
            
        if player == 4 and currentOrder[4] == 1:
            if pk == 1:
                post.p52_makes += 1
                post.team1_cups -= 1
                shotsMadeTurn[4] = 1
                post.save()
            if pk == 0:
                post.p52_misses += 1
                shotsMadeTurn[4] = 0
                post.save()
            
        if player == 5 and currentOrder[5] == 1:
            if pk == 1:
                post.p62_makes += 1
                post.team1_cups -= 1
                shotsMadeTurn[5] = 1
                post.save()
            if pk == 0:
                post.p62_misses += 1
                shotsMadeTurn[5] = 0
                post.save()
            
        shotsTakenTurn += 1
        
        
        #End of Round
        if shotsTakenTurn == numOfShooters:
            shotsTakenTurn = 0
            currentOrder = shotsMadeTurn

            #End of turn
            if sum(shotsMadeTurn) < 2:
                currentTurn = 1
                currentOrder = [1,1,1,1,1,1]
            shotsMadeTurn = [0,0,0,0,0,0]

    #Who Shoots Next, Goes to the shooterName
    
    if player != ([i for i, n in enumerate(currentOrder) if n == 1][-1] + 1):
        nextShooterPos = [i for i, n in enumerate(currentOrder) if n == 1][shotsTakenTurn] + 1
    else:
        nextShooterPos = [i for i, n in enumerate(currentOrder) if n == 1][0] + 1


    shooterName = getattr(post, 'p'+(str(nextShooterPos))+'_team'+str(currentTurn))
    
    
    gameRoster = GameRosters.objects.all()
    print(currentOrder)
    context = {
        'gameRoster': gameRoster,
        'shooterName': shooterName,
        'player1shot': currentOrder[0],
        'player2shot': currentOrder[1],
        'player3shot': currentOrder[2],
        'player4shot': currentOrder[3],
        'player5shot': currentOrder[4],
        'player6shot': currentOrder[5],
        'currentTurn': currentTurn
        }
    return render(request, 'team_view.html', context)
    

def GameReset(request):
    global shotsTakenTurn, shotsMadeTurn, currentOrder

    shotsMadeTurn = [1,1,1,1,1,1]
    currentOrder = [1,1,1,1,1,1]
    shotsTakenTurn = 0
    currentTurn = 1

    post = GameRosters.objects.get(id=1)

    post.p11_makes = 0
    post.p11_misses = 0
    post.p21_makes = 0
    post.p21_misses = 0
    post.p31_makes = 0
    post.p31_misses = 0
    post.p41_makes = 0
    post.p41_misses = 0
    post.p51_makes = 0
    post.p51_misses = 0
    post.p61_makes = 0
    post.p61_misses = 0
    
    post.p12_makes = 0
    post.p12_misses = 0
    post.p22_makes = 0
    post.p22_misses = 0
    post.p32_makes = 0
    post.p32_misses = 0
    post.p42_makes = 0
    post.p42_misses = 0
    post.p52_makes = 0
    post.p52_misses = 0
    post.p62_makes = 0
    post.p62_misses = 0

    post.team2_cups = 100
    post.team1_cups = 100
    post.save()

    return team_players(request)
    #gameRoster = GameRosters.objects.all()
    #context = {
    #    'gameRoster': gameRoster
    #    }
    #return render(request, 'team_players.html', context)

def GameView(request):
    gameRoster = GameRosters.objects.all()
    post = GameRosters.objects.get(id=1)
    shooterName = post.p1_team1
    context = {
        'gameRoster': gameRoster,
        'shooterName': shooterName
    }
    return render(request, 'game_view.html', context)
    

def Undo(request):
    post = GameRosters.objects.get(id=1)
    global shotsMadeTurn, currentOrder, shotsTakenTurn

    
    shotsTakenTurn -= 1
    playerUndone = [i for i, n in enumerate(currentOrder) if n == 1][shotsTakenTurn]

    
    if currentTurn == 1:
        if playerUndone == 0 and currentOrder[0] == 1:
            
            if shotsMadeTurn[0] == 1:
                post.p11_makes -= 1
                post.save()
            else:
                post.p11_misses -= 1
                post.save()
            shotsMadeTurn[0] = 0
           
        if playerUndone == 1 and currentOrder[1] == 1:
            if shotsMadeTurn[1] == 1:
                post.p21_makes -= 1
                post.save()
            else:
                post.p21_misses -= 1
                post.save()
            shotsMadeTurn[1] = 0
            
        if playerUndone == 2 and currentOrder[2] == 1:
            if shotsMadeTurn[2] == 1:
                post.p31_makes -= 1
                post.save()
            else:
                post.p31_misses -= 1
                post.save()
            shotsMadeTurn[2] = 0

        if playerUndone == 3 and currentOrder[3] == 1:
            if shotsMadeTurn[3] == 1:
                post.p41_makes -= 1
                post.save()
            else:
                post.p41_misses -= 1
                post.save()
            shotsMadeTurn[3] = 0

        if playerUndone == 4 and currentOrder[4] == 1:
            if shotsMadeTurn[4] == 1:
                post.p51_makes -= 1
                post.save()
            else:
                post.p51_misses -= 1
                post.save()
            shotsMadeTurn[4] = 0
        
        if playerUndone == 5 and currentOrder[5] == 1:
            if shotsMadeTurn[5] == 1:
                post.p61_makes -= 1
                post.save()
            else:
                post.p61_misses -= 1
                post.save()
            shotsMadeTurn[5] = 0


    if currentTurn == 2:
        if playerUndone == 0 and currentOrder[0] == 1:
            
            if shotsMadeTurn[0] == 1:
                post.p12_makes -= 1
                post.save()
            else:
                post.p12_misses -= 1
                post.save()
            shotsMadeTurn[0] = 0
           
        if playerUndone == 1 and currentOrder[1] == 1:
            if shotsMadeTurn[1] == 1:
                post.p22_makes -= 1
                post.save()
            else:
                post.p22_misses -= 1
                post.save()
            shotsMadeTurn[1] = 0
            
        if playerUndone == 2 and currentOrder[2] == 1:
            if shotsMadeTurn[2] == 1:
                post.p32_makes -= 1
                post.save()
            else:
                post.p32_misses -= 1
                post.save()
            shotsMadeTurn[2] = 0

        if playerUndone == 3 and currentOrder[3] == 1:
            if shotsMadeTurn[3] == 1:
                post.p42_makes -= 1
                post.save()
            else:
                post.p42_misses -= 1
                post.save()
            shotsMadeTurn[3] = 0

        if playerUndone == 4 and currentOrder[4] == 1:
            if shotsMadeTurn[4] == 1:
                post.p52_makes -= 1
                post.save()
            else:
                post.p52_misses -= 1
                post.save()
            shotsMadeTurn[4] = 0
        
        if playerUndone == 5 and currentOrder[5] == 1:
            if shotsMadeTurn[5] == 1:
                post.p62_makes -= 1
                post.save()
            else:
                post.p62_misses -= 1
                post.save()
            shotsMadeTurn[5] = 0


    if playerUndone != ([i for i, n in enumerate(currentOrder) if n == 1][-1] + 1):
        nextShooterPos = [i for i, n in enumerate(currentOrder) if n == 1][shotsTakenTurn] + 1
    else:
        nextShooterPos = [i for i, n in enumerate(currentOrder) if n == 1][0] + 1


    shooterName = getattr(post, 'p'+(str(nextShooterPos))+'_team'+str(currentTurn))
    
    
    gameRoster = GameRosters.objects.all()

    context = {
        'gameRoster': gameRoster,
        'shooterName': shooterName
        }
    return render(request, 'team_view.html', context)

        
        



