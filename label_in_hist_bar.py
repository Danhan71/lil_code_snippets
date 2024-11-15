#Little chunk of code to put the data label inside of a stcaked bar plot
counts,edges,bars = ax[0][2].hist(disp_out.values(),label=disp_out.keys(),bins=disp_xbins,stacked=True)
        color_to_label = {bar[0].get_facecolor(): label for bar, label in zip(bars, disp_out.keys())}        
        for bar_group, dataset_counts in zip(bars, counts):
            for rect in bar_group:
                # Only label bars with non-zero height
                if rect.get_height() > 0:
                    # Determine the label based on the color
                    label = color_to_label.get(rect.get_facecolor(), "Unknown")
                    # Calculate the position for the text
                    x_pos = rect.get_x() + rect.get_width() / 2
                    y_pos = rect.get_y() + rect.get_height() / 2
                    # Add the label
                    ax[0][2].text(x_pos, y_pos, label, ha='center', va='center', color='white', fontsize=8)
