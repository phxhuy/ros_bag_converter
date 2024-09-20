# ros_bag_converter
This package is a collection of note and tools for converting ros 1 bag to ros 2 bag and vice verse

## Purpose

Most of rosbag conversion could work with [rosbags-convert](https://gitlab.com/ternaris/rosbags), unless they have issues in encoding, or the messages are non-standard ROS 2 message.

In this package we aim to solve these corner cases problem via a host of tools, for example, building a new bag file using [images](https://github.com/ethz-asl/kalibr/wiki/bag-format#bagcreater)
