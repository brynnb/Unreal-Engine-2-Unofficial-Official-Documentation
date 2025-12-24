# Adding syntax coloring for Unreal Script

*Original author was Joe Graf ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)). Tweaked slightly and anonymously for better wikiness. Added regedit hack by Christian M. Buhl (ArmyGameTeam?). Jack Porter ([EpicGames](https://udn.epicgames.com/Main/EpicGames)) added the Visual Studio .NET registry file. Maintained by Richard Nalezynski?.*

* [Adding syntax coloring for Unreal Script](#adding-syntax-coloring-for-unreal-script)
  + [Visual Studio .NET 2003 (VC7.1)](#visual-studio-net-2003-vc71))
  + [Visual Studio .NET 2002 (VC7)](#visual-studio-net-2002-vc7))
  + [Visual Studio 6](#visual-studio-6)
    - [Option 1: DLL Installation](#option-1-dll-installation)
    - [Option 2: Altering your registry to allow syntax coloring in UnrealScript](#option-2-altering-your-registry-to-allow-syntax-coloring-in-unrealscript)
  + [Other Tools](#other-tools)
    - [UltraEdit](#ultraedit)

## Visual Studio .NET 2003 (VC7.1)

Download the [Visual-Studio-.NET-2003-UC-Syntax-Highlighting.reg](rsrc/Two/UnrealScriptSyntaxHighlighting/Visual-Studio-.NET-2003-UC-Syntax-Highlighting.reg) registry file and double-click it. Restart Visual Studio.NET. Visual Studio.NET will now perform C++ syntax highlighting on .uc files.

## Visual Studio .NET 2002 (VC7)

Download the [Visual-Studio-.NET-UC-Syntax-Highlighting.reg](rsrc/Two/UnrealScriptSyntaxHighlighting/Visual-Studio-.NET-UC-Syntax-Highlighting.reg) registry file and double-click it. Restart Visual Studio.NET. Visual Studio.NET will now perform C++ syntax highlighting on .uc files.

## Visual Studio 6

### Option 1: DLL Installation

**Adding UWHighlighting.dll to MSDev**Simply place the [UWHighlighting.dll](rsrc/Two/UnrealScriptSyntaxHighlighting/UWHighlighting.dll) file in the `C:\Program Files\Microsoft Visual Studio\Common\MSDev98\AddIns` directory (or wherever your installation is). Then go to the `Tools | Customize...` menu. Choose the `Add-ins and Macros` tab. Enable the add-in entitled `UWHighlighting.DSAddIn.1`.**Step 2: Adding usertype.dat to MSDev**Place the [usertype.dat](rsrc/Two/UnrealScriptSyntaxHighlighting/usertype.dat) file in the `C:\Program Files\Microsoft Visual Studio\Common\MSDev98\Bin` directory.**Step 3: Seeing it in action**Restart Visual Studio. Open your favorite UC file and see the Unreal keywords appear in blue (or whatever you have them set to).**Adding keywords**To add a missing keyword, simply edit the [usertype.dat](rsrc/Two/UnrealScriptSyntaxHighlighting/usertype.dat) file and place the missing keyword on its own line. For instance:

```

native
...
missingKeyword
```

Remember to restart Visual Studio to see the new keyword, and please consider updating the file here with your new version (just make a note here in the doc of what you added)!

### Option 2: Altering your registry to allow syntax coloring in UnrealScript

As far as I can tell, this does exactly what the DLL is supposed to do. The `usertype.dat` file is still useful though.**Step 1. Run Regedit**Type `regedit` in the *Run* window or from a command line.**Step 2. Find the tag**`HKEY_CURRENT_USER\Software\Microsoft\DevStudio\6.0\Text Editor\Tabs/Language Settings\C/C++\FileExtensions`**Step 3. Add ;uc to the end of the tag**So the Value data should look something like this:
`cpp;cxx;c;h;hxx;hpp;inl;tlh;tli;rc;rc2;uc`

## Other Tools

### UltraEdit

*[UltraEdit](http://www.ultraedit.com/) is a pretty inexpensive and decent text editor for windows, from <http://www.ultraedit.com> It reminds some of Visual Slick Edit, but without the crazy pricetag. :)*A [UnrealScriptUltraeditWords.txt](rsrc/Two/UnrealScriptSyntaxHighlighting/UnrealScriptUltraeditWords.txt) words file for [UltraEdit](http://www.ultraedit.com/) (version 10) has been attached. To use it simply append it to your existing wordsfile.txt in the directory [UltraEdit](http://www.ultraedit.com/) was installed to. This wordsfile uses language #20 like all the downloadable words files from the [UltraEdit](http://www.ultraedit.com/) web site, so you might have to give it a new language number by editing the first few characters of this file and changing the /L20 into /L13 or some other unused number. You will need to also edit the settings under Advanced/Configuration/FileTypes and add UnrealScript Files(\*.uc) to it. You should probably customize the colors under the Syntax Highlighting tab, as the words file includes more categories than the normal scheme handles well (some colors are duplicated like red if you don't customize them).

