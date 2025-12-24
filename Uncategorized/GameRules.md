# GameRules Documentation

*Document Summary: Describes some important elements of the GameInfo class, which is responsible for the game logic.**Document Changelog: Last updated by Michiel Hendriks, added some more information. Previous update by Richard 'vajuras' Osborne ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)), for document creation.*

* [GameRules Documentation](GameRules.md#gamerules-documentation)
  + [GameInfo Objects](GameRules.md#gameinfo-objects)
    - [Important variables](GameRules.md#important-variables)
    - [Function Breakdown](GameRules.md#function-breakdown)
  + [Sample Gametype](GameRules.md#sample-gametype)

## GameInfo Objects

Gametypes offer gamers different styles of play. The rules and components that compose a gametype is defined by a **GameInfo** object (Engine.GameInfo). GameInfo objects and many of it's subcomponents exists absolutely on the server (Level.Game is always None on the client during a network game) and therefore, is the authority on damage, player starts, bots, and many other components that are critical to gameplay. All gameplay decisions are always handled on the server and the current state of the game is replicated to all clients connected to the game through the **GameReplicationInfo** object.

### Important variables

There are many variables in the GameInfo class. Here are some important variables responsible for additional components in the game.

GameReplicationInfoClas (GRI)
:   Sets the GRI class to use. The GRI replicates information about the state of the server's GameInfo object to all clients connected to the game. The GRI is always relevant to every client connected to the game (in case you are wondering why it's because it's *bAlwaysRelevant* property is set to true) so any information that the client needs to be aware of about the gametype should be defined and replicated here (such as the current score, Time Limit, etc). Client's are even unaware of the gametype, whether it's deathmatch or CTF (unless they use the GameName variable). The GRI class to be used is set by the `GameReplicationInfoClass` variable.

PlayerControllerClassName
:   Defines the type of PlayerController that all human players (clients) will use.

BaseMutator
:   refers to the *root* mutator. Mutators can make many major/minor modifications to gameplay. The intention is for gamers to pick the desired mutator via the menu and they get added to the gametype at game start.

MutatorClass
:   The initial mutator to spawn, this will be the BaseMutator. Unless you need some logic in a base mutator this should point to "Engine.Mutator".

AccessControlClass
:   The AccessControl class to use. The AccessControl? component takes care of the user management, wether they can become admins or are even allowed to join the game.

GameRulesModifiers
:   A linked list of GameRules classes. GameRule are much like mutators except that they can only modify some of the rules of the current game (like checking the end game condition or modifying scoring rules).

DeathMessageClass
:   Contains death messages (how the victim was killed)

GameMessageClass
:   Contains messages related to Game specific events

BroadcastHandlerClass
:   The BroadcastHandler class to use. The BroadcastHandler is reponsible for delivering messages (both text as LocalMessage). It can be used to filter messages for some users.

HUDType
:   HUD class this game uses.

VoiceReplicationInfoClass
:   The class responsible for replicating information about the built in voice chat features (like available channels). (v3323 and up).

MaplistHandler
:   This class manages the map list, e.g. what map comes next (set via `MaplistHandlerType` and `MaplistHandlerClass`). Not useful for single player games.

VotingHandler
:   Provides functionality for in-game voting, things to vote on can be the next map or to kick a player (set by `VotingHandlerType` and `VotingHandlerClass`). VotingHandler is only useful for multi player games.

### Function Breakdown

Below are some functions that are critical to gameplay. The GameInfo object is very well commented, so we will only cover a small subset here:

InitGame
:   The GameInfo's InitGame() function is called before any other scripts (including PreBeginPlay() ), and is used by the GameInfo to initialize parameters and spawn its helper classes. You should parse the commandline\url here for settings.

ProcessServerTravel
:   notification that the server is changing levels.

PreLogin
:   This will be called when a player tries to join the game. It can be used to reject a player.

Login
:   Occurs when a client has officially joined the game. In this function the player's avatar should be created and stuff like that.

PostLogin
:   Called after a succesful *Login*. It is the first place that is safe to call replicated functions on the PlayerController.

Logout
:   Called when a player left the game (for whatever reason).

## Sample Gametype

For a sample gametype read the [MyFirstGameInfo](MyFirstGameInfo.md) document.
