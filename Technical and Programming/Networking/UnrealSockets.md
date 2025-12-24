# Unreal Sockets

*Document Summary: Explains the unrealscript networking classes TCPLink and UDPLink.**Document Changelog: Created by Michiel Hendriks, to complete the [NetworkingTome](https://udn.epicgames.com/Two/NetworkingTome).*

* [Unreal Sockets](#unreal-sockets)
  + [Overview](#overview)
  + [InternetLink](#internetlink)
    - [LinkMode](#linkmode)
    - [Line mode](#line-mode)
    - [ReceiveMode](#receivemode)
    - [Resolving hostnames](#resolving-hostnames)
    - [IsDataPending](#isdatapending)
    - [GetLastError](#getlasterror)
    - [IpAddrToString and StringToIpAddr](#ipaddrtostring-and-stringtoipaddr)
    - [ParseURL](#parseurl)
    - [GetLocalIP](#getlocalip)
  + [Common elements](#common-elements)
    - [BindPort](#bindport)
  + [TcpLink](#tcplink)
    - [AcceptClass](#acceptclass)
    - [LinkState](#linkstate)
    - [Listen](#listen)
    - [Open](#open)
    - [Close](#close)
    - [IsConnected](#isconnected)
    - [SendText](#sendtext)
    - [SendBinary](#sendbinary)
    - [ReadText](#readtext)
    - [ReadBinary](#readbinary)
    - [Accepted](#accepted)
    - [Opened](#opened)
    - [Closed](#closed)
    - [ReceivedText](#receivedtext)
    - [ReceivedLine](#receivedline)
    - [ReceivedBinary](#receivedbinary)
  + [UdpLink](#udplink)

## Overview

If you don't want to delve into the TCP/UDP fundamentals to create a C++ implementation, it will be easiest to write your code using the UnrealScript? interface. Since most network transmissions are not CPU-bound, this shouldn't be a problem.The engine provides unrealscript interfaces to work with both UDP ([UDPLink](#udplink)) and TCP ([TCPLink](#tcplink)) sockets. They can be used as clients and as servers.As with everything you might want to take a look at some of the existing implementations for more information.

## InternetLink

Both the ([TCPLink](#tcplink)) and ([UDPLink](#udplink)) subclass from this class. This class declares a few important functions (like hostname resolving) and types. Most of the variables declared here, except for the few described below, are only to be used from the native implementation of the classes.

### LinkMode

```

var enum ELinkMode
{
   MODE_Text,
   MODE_Line,
   MODE_Binary
} LinkMode;
```

This variable defines what events will be triggered when data is received.

MODE\_Text
:   data send via *SendText* is send AS IS, the event *ReceivedText* is called when text is received

MODE\_Line
:   data send via *SendText* will get newline tokens appended, the event *ReceivedLine* is called when a line is received (excluding the newline tokens)

MODE\_Binary
:   when data is received the *ReceivedBinary* event will be called. UnrealScript? hasn't been designed to properly handle binary data. Because of this the functionality to use binary data in sockets is rather limited.

This variable has to be set after the class has been spawned. It can be changed at any time.

### Line mode

```

var enum ELineMode
{
   LMODE_auto,
   LMODE_DOS,   // CRLF
   LMODE_UNIX, // LF
   LMODE_MAC,   // LFCR
} InLineMode, OutLineMode;
```

Only used in case of `LinkMode = MODE_Line`. It defines when a line is detected and what tokens are appended in case of a *SendText*. In line endings are not important you should use `LMODE_auto` for `InLineMode`, in this case only a line feed is significant for a newline, a leading or trailing carriage return is removed. `LMODE_auto` for `OutLineMode` equals to `LMODE_DOS`.

### ReceiveMode

```

var enum EReceiveMode
{
   RMODE_Manual,
   RMODE_Event
} ReceiveMode;
```

This defines how data is read. With `RMODE_Event` events are triggered when data is received, with `RMODE_Manual` you should check for data yourself and read it manually.

### Resolving hostnames

In order to connect to a remote host unreal requires an <nopIpAddr struct. However, usually the only thing you've got is the port number and a hostname. This hostname first has to be resolved. For this the function *resolve()* has been declared:

```

native function Resolve( coerce string Domain );
```

You can pass both a hostname or a IP address (as a string) and it will resolve it to an IpAddr struct. When the resolve was succesful the *Resolved* event will be triggered, otherwise the *ResolveFailed* event will be triggered.Usually resolving a hostname will block the rest of the process until the resolve has been finished. This is not desireable in this case. Therefore hostname resolving has been made unblocking (this is done by starting a new thread for the resolve). Because the *resolve* function returns before the resolve is actually done you shouldn't do anything until you either receive a *resolved* or *resolvefailed* event.

### IsDataPending

```

native function bool IsDataPending();
```

Returns true when there is data to be read. This is only useful when manually reading data instead of using the event based reading.

### GetLastError

```

native function int GetLastError();
```

This will return the last socket error. The value is the value as returned by the operating system, so you might want to look up the error code in the OS's documentation. (Or use a web searchengine)

### IpAddrToString and StringToIpAddr

```

native function string IpAddrToString( IpAddr Arg );
native function bool StringToIpAddr( string Str, out IpAddr Addr );
```

This will convert an IpAddr to a string and vice versa. *StringToIpAddr* only works for strings like `12.123.45.78:7777`. For hostnames you should use the *Resolve* function.

### ParseURL

```

native function bool ParseURL
(
   coerce string URL,
   out string Addr,
   out int Port,
   out string LevelName,
   out string EntryName
);
```

This will parse an string as an URL (returning true when valid). This function is only useful for unreal style URLs, it is not very useful for the common URIs.

### GetLocalIP

```

native function GetLocalIP(out IpAddr Arg );
```

Returns the IP of the local machine (the one it's bound to).

## Common elements

Both TCPLink and UDPLink share a few identical functions and events that are not defined in their parent classes.

### BindPort

```

native function int BindPort( optional int Port, optional bool bUseNextAvailable );
```

One of the most important functions. This function will bind a port to be used for communication. Only in case of a server socket you should provide a port number to bind to. In case the provided port can not be bound (because it's already bound by an other process) it will issue an error, unless `bUseNextAvailable` is true, then it will bind the next available port. The function will return the port number is has bound to.

## TcpLink

A TCPLink can be used in two ways, as a client or as a server. To use it as a client you should call *BindPort* and then *Open*, to use it as a server you should call *BindPort* and then *Listen*. For a server you might also want to consider to use an `AcceptClass` to handle the actual communication when a client connected to the server because a single class hasn't been designed to handle multiple clients.

### AcceptClass

```

var class<TcpLink> AcceptClass;
```

If `AcceptClass` is not `None`, an actor of class `AcceptClass` will be spawned when an incoming connecting is accepted, leaving the listener open to accept more connections. *Accepted()* is called only in the child class. You can use the *LostChild()* and *GainedChild()* events to track your children.

### LinkState

```

var enum ELinkState
{
   STATE_Initialized,      // Sockets is initialized
   STATE_Ready,         // Port bound, ready for activity
   STATE_Listening,      // Listening for connections
   STATE_Connecting,      // Attempting to connect
   STATE_Connected,      // Open and connected
   STATE_ListenClosePending,       // Socket in process of closing
   STATE_ConnectClosePending,      // Socket in process of closing
   STATE_ListenClosing,           // Socket in process of closing
   STATE_ConnectClosing           // Socket in process of closing
} LinkState;
```

The current state of the socket. Set by native code and should only be read.

### Listen

```

native function bool Listen();
```

Start listening for incomming connections. For a server link you should call this function after *BindPort*. A single class can only handle a few connectings at the same time. It's best to create an `AcceptClass` that does the actual processing.

### Open

```

native function bool Open( IpAddr Addr );
```

Open a connection to a remote host. This is meant to be used for TCP client after *BindPort* has been called. Returns true when successful.

### Close

```

native function bool Close();
```

Close the current connection. Returns true when successful.

### IsConnected

```

native function bool IsConnected();
```

Returns true if connected.

### SendText

```

native function int SendText( coerce string Str );
```

Send `str` to the connected peer. If `LinkMode` is `MODE_Line` a newline token is appended. Returns the number of bytes actually send.

### SendBinary

```

native function int SendBinary( int Count, byte B[255] );
```

Send a piece of binary data to the remote peer. `Count` specifies the number of bytes in `B` to send. Returns the number of bytes send.

### ReadText

```

native function int ReadText( out string Str );
```

Read a string from the buffer. This function is to be used with `RecieveMode` set to `RMODE_Manual`. Returns the number of bytes read.

### ReadBinary

```

native function int ReadBinary( int Count, out byte B[255] );
```

Read `Count` (with a max of `255`) bytes from the buffer. This function is to be used with `RecieveMode` set to `RMODE_Manual`. Returns the number of bytes read.

### Accepted

```

event Accepted();
```

Called during `STATE_Listening` when a new connection is accepted.

### Opened

```

event Opened();
```

Called when socket successfully connects.

### Closed

```

event Closed();
```

Called when *Close()* completes or the connection is dropped.

### ReceivedText

```

event ReceivedText( string Text );
```

Called when data is received and connection mode is `MODE_Text`.

### ReceivedLine

```

event ReceivedLine( string Line );
```

Called when data is received and connection mode is `MODE_Line`.

### ReceivedBinary

```

event ReceivedBinary( int Count, byte B[255] );
```

Called when data is received and connection mode is `MODE_Binary`.

## UdpLink

UDPLink's functions are almost identical to those of TCPLink with a major exception: they all take an extra argument of type `IpAddr`. This is the destination or source to use. Since UDP is a connectionless protocol a single class can be connected to more than one remote peer at the same time without any issues. So there's no need for an accept class or similar things.Implemented functions are: SendText, SendBinary, ReadText, ReadBinary.Implemented events are: ReceivedText, ReceivedLine, ReceivedBinary.The only thing you need to do to use an UDPLink is call *BindPort* and start sending\recieving data. There's no direct difference between an UDP client and UDP server (except that for a server you should specify a port number to bind to).

