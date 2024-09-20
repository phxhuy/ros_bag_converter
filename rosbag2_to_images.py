import os
import cv2
import time  # Import time module to get system time
from cv_bridge import CvBridge
from sensor_msgs.msg import Image as ROS2Image
from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions
from rclpy.serialization import deserialize_message

def save_images_from_ros2_bag(ros2_bag_path, image_topic, output_folder):
    """Saves images from a ROS2 bag to the specified output folder."""
    
    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize ROS2 reader
    reader = SequentialReader()
    
    storage_options = StorageOptions(uri=ros2_bag_path, storage_id='sqlite3')
    converter_options = ConverterOptions('', '')
    reader.open(storage_options, converter_options)
    
    bridge = CvBridge()
    image_count = 0
    
    try:
        while reader.has_next():
            (topic, data, t) = reader.read_next()
            
            # Check if the message is from the specified image topic
            if topic == image_topic:
                # Deserialize the message as a ROS2 Image
                ros2_image = deserialize_message(data, ROS2Image)

                # Extract the timestamp from the ROS2 message (in nanoseconds)
                # timestamp_sec = ros2_image.header.stamp.sec
                # timestamp_nanosec = ros2_image.header.stamp.nanosec
                # # Convert to a full timestamp with decimal seconds
                # timestamp = timestamp_sec + timestamp_nanosec * 1e-9

                
                current_time = int(time.time())
                
                # Convert ROS2 Image to OpenCV image
                cv_image = bridge.imgmsg_to_cv2(ros2_image, desired_encoding='passthrough')
                
                # Save image to the output folder
                # image_filename = os.path.join(output_folder, f"frame_{image_count:04d}.png")
                
                # Format the timestamp as a filename-friendly string
                image_filename = os.path.join(output_folder, f"{current_time}.png")

                cv2.imwrite(image_filename, cv_image)
                print(f"Saved {image_filename}")
                
                image_count += 1
    finally:
        print(f"Total images saved: {image_count}")

if __name__ == '__main__':
    ros2_bag_path = '/home/huy/Upteko_ws/software/camera_caliberation/siyiA8mini_camera_calib_recording 1/rosbag2_2024_09_18-12_34_20_0.db3'  # Replace with your ROS2 bag path
    image_topic = '/camera/image_raw'  # Replace with your image topic
    output_folder = './dataset_1/cam0'  # Folder where images will be saved

    # Save images from the ROS2 bag
    save_images_from_ros2_bag(ros2_bag_path, image_topic, output_folder)
