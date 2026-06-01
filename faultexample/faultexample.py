from scalesim.scale_sim import scalesim

s = scalesim(save_disk_space=True,
                 verbose=True,
                 config='google.cfg',
                 topology='../topologies/conv_nets/test.csv',
                 layout='../layouts/conv_nets/test.csv',
                 input_type_gemm=False)
s.run_scale(top_path='./out')