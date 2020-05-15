from django.shortcuts import render
from django.views import View
from random import randint

from .forms import AttemptForm
from .models import Player, Game, PlayerGameInfo


class ShowHomeView(View):

    def get_or_create_game(self, player, game_id):
        game = Game.objects.filter(id=game_id)
        if game.exists():
            return game.first()
        active_games = Game.objects.filter(is_active=True)
        if active_games:
            game = active_games.first()
            PlayerGameInfo.objects.create(player=player, game=game)
            return game
        game = Game.objects.create(number=randint(-100, 100))
        PlayerGameInfo.objects.create(player=player, game=game, is_author=True)
        return game


    def get(self, request):
        player_id = request.session.get('player_id')
        game_id = request.session.get('game_id')

        player, _ = Player.objects.get_or_create(id=player_id)
        request.session['player_id'] = player.id

        game = self.get_or_create_game(player, game_id)
        request.session['game_id'] = game.id
        relation = PlayerGameInfo.objects.get(player=player, game=game)

        if relation.is_author:
            context = {'number': game.number}
            if not game.is_active:
                del request.session['game_id']
                attempts = PlayerGameInfo.objects. \
                    filter(game=game, is_author=False, win=True). \
                    values_list('attempts_num', flat=True)
                context['attempts'] = attempts
        else:
            context = {'form': AttemptForm}

        return render(request, 'home.html', context=context)

    def post(self, request):
        player = Player.objects.get(id=request.session['player_id'])
        game = Game.objects.get(id=request.session['game_id'])
        relation = PlayerGameInfo.objects.filter(player=player, game=game).first()

        form = AttemptForm(request.POST)
        if form.is_valid():
            relation.attempts_num += 1
            relation.save()
            form_number = form.cleaned_data['number']
            if form_number == game.number:
                game.is_active = False
                game.save()
                relation.win = True
                relation.save()
                del request.session['game_id']
                message = 'Вы угадали число!'
            elif game.number < form_number:
                message = f'Загаданное число меньше числа {form_number}'
            else:
                message = f'Загаданное число больше числа {form_number}'
        else:
            message = 'Введите корректное число'

        return render(
            request,
            'home.html',
            context={
                'form': AttemptForm,
                'message': message
            })
