# Scripted Sequences Tutorial

*Document Summary: A brief guide to using Scripted Sequences.**Document Changelog: Last updated by Chris Linder (DemiurgeStudios?). Original author was Hugh Macdonald ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).*

* [Scripted Sequences Tutorial](#scripted-sequences-tutorial)
  + [Overview](#overview)
    - [Using a Dynamic Array](#using-a-dynamic-array)
    - [Using the ScriptedSequence](#using-the-scriptedsequence)
  + [Related Documents](#related-documents)

## Overview

Scripted Sequences are used to control pawns in scenes. In your ScriptedSequence actor, under **AIScript** is a dynamic array of **[Actions](ScriptedSequenceActions.md)**.

### Using a Dynamic Array

Initially, your Actions array will be empty. To add a new action, click on **Add**. This will create an empty element in the array (**Add** will always create elements at the end of the array). If, at any point, you click on **Empty**, it will clear the whole array, and you will lose any data that was in it.Once you have an empty element in the array, you can expand it, and get a drop-down box which lists all the items which can be added into the array. To create a specific item for the array, select the item you wish to use from the drop-down-box, and click on **New**. The item that has been created can then be expanded to allow access to its variables.To clear an element in the array, go to the main holder for that element (with the array index, eg **[1]**), and click on **Clear**. This will leave the actual element, but remove all the contents. To remove an element completely, click on **Delete**. If you wish to insert a new element before the current one, you can click on **Insert**.To change the contents of an element, you must clear it first, and then create the new content.

### Using the ScriptedSequence

To link a pawn to a ScriptedSequence, you need to set the pawn's **AIScriptTag** to the **Tag** of the ScriptedSequence. This will cause the sequence to start executing as soon as the pawn is active in the level (usually as soon as the level begins). Because of this, the most useful command to have first in the ScriptedSequence is a **WaitForEvent**. Once you have set this, you can then wait to trigger the rest of the sequence.Any actions that you can use in a ScriptedSequence are described fully in the [Actions](ScriptedSequenceActions.md) doc.

## Related Documents

[ScriptedSequenceActions](ScriptedSequenceActions.md) - This document talks about the types of actions ScriptedSequences can do.[AIControllers](AIControllers.md) - This document goes over all the types of AIControllers as well as how to set up AIControllers in Unrealed.AIReferenceDocument? - This document talks about the technical side of AI. It goes over Controllers, AIControllers, and ScriptedControllers, as well as AIScripts and ScriptedSequences.

