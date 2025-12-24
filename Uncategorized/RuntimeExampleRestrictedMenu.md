# Runtime Example Restricted Menu

*Created by Chris Linder (DemiurgeStudios?) on 10-21-03 for the Unreal Runtime. Last Updated by Chris Linder (DemiurgeStudios?).*

* [Runtime Example Restricted Menu](RuntimeExampleRestrictedMenu.md#Runtime Example Restricted Menu)
  + [Related Documents](RuntimeExampleRestrictedMenu.md#Related Documents)
  + [Introduction](RuntimeExampleRestrictedMenu.md#Introduction)
  + [Creating the Main Menu](RuntimeExampleRestrictedMenu.md#Creating the Main Menu)
  + [Creating the In-Game Menu](RuntimeExampleRestrictedMenu.md#Creating the In-Game Menu)
  + [Creating the Restricted Console](RuntimeExampleRestrictedMenu.md#Creating the Restricted Console)
  + [Installing the Example](RuntimeExampleRestrictedMenu.md#Installing the Example)

## Related Documents

[GuiReference](../Technical and Programming/User Interface/GuiReference.md), [LocalizationReference](../Technical and Programming/User Interface/LocalizationReference.md)

## Introduction

This example will go over how to create an example menu that limits access to the engine and engine settings. A menu such as this would be appropriate for computers placed in a museum or educational setting for example. As well as creating a simple menu, this example goes over how to restrict the console so that commands can not be typed in. This example is based on the Unreal Runtime but it can be used in any 2226 or higher build of the engine.

## Creating the Main Menu

![MainMenu.jpg](../assets/MainMenu.jpg)

The main menu was designed to be very simple. It does not have any tabs, any game settings, any controller settings, or even a button to exit the game. The game can be exited by closing the window. (If the game is fullscreen, press "alt-enter" to make the game not fullscreen, and then you can close it.)The menu has a title, a map list with a heading, and a load button. The up and down arrows can be used to select the map. To load the map either the load button can be click, enter can be pressed, or the map name can be double clicked. The last map loaded is saved and is highlighted when the main menu is shown again. This includes between map loads and exiting the game and re-launching it. See the [well documented code](rsrc/Two/RuntimeExampleRestrictedMenu/ExampleMenuRestricted.zip) for implementation details.

## Creating the In-Game Menu

![MidGameMenu.jpg](../assets/MidGameMenu.jpg)

The mid-game menu was also designed to be very simple. It pauses the game and gives you the choice to either continue the game, or close the map and return to the main menu. You can continue the game and close the mid-game menu by either clicking the "CONTINUE" button, selecting the "CONTINUE" button with the keyboard and pressing 'Enter', or hitting 'Esc'. You can close the map and return to the main menu by either clicking the button or moving the selection to that button and pressing 'Enter'. See the [well documented code](rsrc/Two/RuntimeExampleRestrictedMenu/ExampleMenuRestricted.zip) for implementation details.

## Creating the Restricted Console

*RestrictedConsole* is very simple; it extends *Engine.Console* override *KeyEvent* so that the key press to bring up the console is ignored. It also overrides *Type*, *Talk*, and *TeamTalk* so that none of these call `GotoState('Typing')`.The engine needs a console, which must be a subclass of *Console*, to work. If there is no console specified in *UE2Runtime.ini*, in the `[Engine.Engine]` section, the game with not launch. If the console specified is not a subclass of *Console*, the engine with launch but maps will not load.

## Installing the Example

Download the [attached zip file](rsrc/Two/RuntimeExampleRestrictedMenu/ExampleMenuRestricted.zip) and unzip it in your Runtime directory. Next you will need to alter your INI file settings to use the new menus and console. In *UE2Runtime.ini*, in the `[Engine.Engine]` section, change the console to:

```

Console=ExampleMenuRestricted.RestrictedConsole
```

Next, in the `[Engine.GameEngine]` section, change the menu classes to:

```

InitialMenuClass=ExampleMenuRestricted.RestrictedMainMenu
MainMenuClass=ExampleMenuRestricted.RestrictedMainMenu
```

Now in *User.ini*, in the `[Engine.PlayerController]` section change the mid game menu to:

```

MidGameMenuClass=ExampleMenuRestricted.RestrictedMidGameMenu
```

At this point you can launch the Runtime and you will see the new menus. If you want to make changes to these menus, make sure you add "ExampleMenuRestricted" to the EditPackages lists in *UE2Runtime.ini*.
