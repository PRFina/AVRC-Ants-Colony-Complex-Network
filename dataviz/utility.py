import collections

def add_legend(fig, axes, on_fig=False):
    legend_x_offset = .025
    legend_y_offset = .0
    legend_bbox = (1.+legend_x_offset, 1.+legend_y_offset)
    if on_fig:
        subplots_legend_handles = []
        subplots_legend_labels = []
        new_labels = []
        new_handles= []
        
        # collect legend handles-labels from every subplot
        for ax in axes:
            handles, labels = ax.get_legend_handles_labels()
            subplots_legend_handles.extend(handles)
            subplots_legend_labels.extend(labels)
        # remove duplicated handles - labels
        for handle, label in zip(subplots_legend_handles, subplots_legend_labels):
            if label not in new_labels:
                new_labels.append(label)
                new_handles.append(handle)

        fig.legend(new_handles, new_labels, loc="upper left", bbox_to_anchor=legend_bbox)
    else:
        if isinstance(axes, collections.abc.Iterable):
            for ax in axes.ravel():
                ax.legend(loc="upper left", bbox_to_anchor=legend_bbox)
        else:
            axes.legend(loc="upper left", bbox_to_anchor=legend_bbox)

    fig.tight_layout()


def set_axis(ax, xlabel, ylabel, log_scale=(False,False)):
  ax.set(xlabel=f"{xlabel}", ylabel=f"{ylabel}") # default
  
  if log_scale[0] and log_scale[1]: #loglog
    ax.set(xlabel=f"{xlabel} (log)", ylabel=f"{ylabel} (log)", xscale="log", yscale="log")
  elif log_scale[0]: #semilog on x
    ax.set(xlabel=f"{xlabel} (log)", ylabel=ylabel, xscale="log")
  elif log_scale[1]: #semilog on y
    ax.set(xlabel=xlabel, ylabel=f"{ylabel} (log)", yscale="log")