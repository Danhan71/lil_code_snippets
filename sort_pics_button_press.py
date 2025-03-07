def get_key(self):
        """
        Function to get user input for the "GUI"
        """
        from pynput import keyboard
        key_pressed = []
        def on_press(key):
            try:
                # Check if the key is good
                if key.char in ['1','2','9','0']:
                    # Convert the key to an integer and store it
                    key_pressed.append(int(key.char))
                    return key_pressed
            except AttributeError:
                pass
                print("Enter valid key")

        def on_release(key):
            # Stop the listener once a valid key is pressed
            try:
                # Check if the key is good
                if key.char in ['1','2','9','0']:
                    # Convert the key to an integer and store it
                    return False
            except AttributeError:
                pass
                print("Enter valid key")

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        if key_pressed:
            return key_pressed[0]  
        else:
            print("Label issue please repeat key stroke")
            return self.get_key()
        
        # Return the stored key
    
    def review_reprojected_frames(self,frames_list, add=60):
        '''
        Function to review reprojected frmaes to pick the good ones
        '''
        from PIL import Image
        frames_dict = {}
        i = 0
        good_hits = 0
        print(frames_list)
        while (i < len(frames_list) and good_hits < add):
            print("loop")
            frame = frames_list[i]
            print(frame)
            with Image.open(frame) as im:
                plt.figure(figsize=(20,20))
                plt.imshow(im,aspect='auto')
                plt.axis('off')
                plt.tight_layout()
                plt.show(block=False)
                plt.draw()
                plt.pause(0.5)
                print("""########################## \n
                Swipe left for bad frame (hit 1 key) \n
                Swipe right for good frame (hit 2 key) \n
                Or mv fwd/bkwd(9/0) \n
                btw hitting 9 subtract 1 from selected good frames count \n
                lazy behavior but its to ensure we get at least the num frames wanted \n
                per vid, in the case where you go back and change from good to bad""")
                print(f"Doing image: {i}")
                print(f"Good frames so far: {good_hits}")
                response = self.get_key()
                print(f"You entered: {response}")
                if response == 9:
                    i = i-1
                    good_hits = good_hits-1
                elif response == 0:
                    i = i+1
                else:
                    frames_dict[f"{frame}"] = response
                    i = i+1
                    if response == 2:
                        good_hits = good_hits+1
                plt.close()
        #Get list of just frame names that are good
        good_frames_list = [k.split('/')[-1] for k,v in frames_dict.items() if v == 2]
        return good_frames_list
