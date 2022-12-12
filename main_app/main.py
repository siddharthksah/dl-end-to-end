# @author Siddharth
# @website www.siddharthsah.com

# importing the necessary packages
from datetime import datetime
import streamlit as st






# favicon and page configs
favicon = './assets/icon.png'
st.set_page_config(page_title='Demo App', page_icon = favicon)
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 140px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 140px;
        margin-left: -140px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#####################################################################
#####################################################################


#####################################################################
#####################################################################
# =====================================================================================
# =====================================================================================


# title of the webapp
#original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Project ECLIPSIS Demo: Extremely Compact DNNs for Edge Intelligence</p>'
#st.markdown(original_title, unsafe_allow_html=True)
#st.title("Project ECLIPSIS Demo: Extremely Compact DNNs for Edge Intelligence")

# =====================================================================================
# =====================================================================================

# Space out the maps so the first one is 2x the size of the other three
left_side_column, right_side_column = st.columns(2)

with left_side_column:

	# st.image("/media/hung/sidd/demo_v3/assets/right_arrow.png", use_column_width  = True)

	# =====================================================================================
	# =====================================================================================

	selectedSidebar = st.radio(
		" ",
		("Image Enhacement", "Speech to Text", "YouTube Sentiment Analysis"), horizontal=True)
	# =====================================================================================
	# =====================================================================================
	if selectedSidebar == "Image Ehancement":

		# =====================================================================================
		# increasing the text size of tab
		font_css = """
		<style>
		button[data-baseweb="tab"] {
		font-size: 14px;
		}
		</style>
		"""
		st.write(font_css, unsafe_allow_html=True)
		# =====================================================================================

		# name of the tabs
		tab_options = ["EfficientNetB0 vs AlphaNetL3", "EfficientNetB3 vs AlphaNetU7"]
		tab_EfficientNetB0_AlphaNetL3, tab_EfficientNetB3_AlphaNetU7 = st.tabs(
			tab_options)

		# batch size options
		batchsize_array = ["128", "64", "32", "16", "8", "4", "2", "1"]

		with tab_EfficientNetB0_AlphaNetL3:
			# st.header("EfficientNetB0")

			# renderData("100 Classes, MFLOPS = 386")

			#st.write("Please select the inference parameters")

			batchSize = st.selectbox(
				'Choose  the batchsize',
				batchsize_array, key="EfficientNetB0_AlphaNetL3_batchsize")

			modelPrecision = "FP32"
			#modelPrecision = st.radio(
			#	"",
			#	('FP32', 'FP16'), horizontal=True, label_visibility="collapsed", key="EfficientNetB0_AlphaNetL3_modelPrecision")

			cpu_gpu = "GPU"
			#cpu_gpu = st.radio(
			#	"",
			#	('CPU', 'GPU'), horizontal=True, label_visibility="collapsed", key="EfficientNetB0_AlphaNetL3_cpu_gpu")

			# model_name = "EfficientNetB0"

			# st.write('You selected:', batchSize, cpu_gpu, modelPrecision)
			
			st.success("Running with FP32 Precision on GPU")

			benchmark = st.button("Benchmark", key="EfficientNetB0_AlphaNetL3_benchmark")

			if benchmark:
				fps_array_efficientnet_b0 = []
				fps_array_AlphaNetL3 = []
				time_array = []
				if cpu_gpu == "CPU":
					cpu_gpu = 'cpu'
				else:
					cpu_gpu = 'cuda'
				count = 0
				stop_button = False
				stop_button = st.button("Stop")
				while (stop_button == False):
					with st.spinner("Processing..."):
						count = count + 1
						
						all_result_efficientnet_b0, mflops_efficientnet_b0, mparam_efficientnet_b0 = inference_efficientnet_b0(
							int(batchSize), cpu_gpu)
						fps_efficientnet_b0 = int(all_result_efficientnet_b0)
						fps_array_efficientnet_b0.append(int(fps_efficientnet_b0))

						singaporeTz = pytz.timezone("Asia/Singapore")
						now = datetime.now(singaporeTz)
						current_time = now.strftime("%H:%M:%S")
						time_array.append(current_time)


						
						all_result_AlphaNetL3, mflops_AlphaNetL3, mparam_AlphaNetL3 = inference_alphanet_l3(
							int(batchSize), cpu_gpu)
						fps_AlphaNetL3 = int(all_result_AlphaNetL3)
						fps_array_AlphaNetL3.append(int(fps_AlphaNetL3))


						try:
							info_placeholder_1.empty()
							info_placeholder_2.empty()
							fps_placeholder.empty()
							# fps_placeholder = st.success("EfficientNetB0 and Hybrid FPS on the currrent batch is " + str(int(fps_effb0)) + " and " + str(int(fps_hybrid)) + " respectively.")
						except:
							pass
						
						info_placeholder_1 = st.info(
							str("EfficientNetB0 - " + "MFLOPS - " + str(mflops_efficientnet_b0) + " , " + "MPARAM - " + str(mparam_efficientnet_b0)))

						info_placeholder_2 = st.info(
							str("AlphaNetL3 (Improved Sampling – Low Flop) + Hybrid (0.23) - " + "MFLOPS - " + str(mflops_AlphaNetL3) + " , " + "MPARAM - " + str(mparam_AlphaNetL3)))



						fps_placeholder = st.success("EfficientNetB0 and AlphaNetL3 FPS on the currrent batch is " + str(int(fps_efficientnet_b0)) + " and " + str(int(fps_AlphaNetL3)) + " respectively.")

						
						
						fps_array_effb0_np = np.array(fps_array_efficientnet_b0)
						fps_array_hybrid_np = np.array(fps_array_AlphaNetL3)
						time_array_np = np.array(time_array)

						df = pd.DataFrame({'EfficientNetB0':fps_array_effb0_np, 'AlphaNetL3':fps_array_hybrid_np, 'time': time_array_np})

						# st.write(df)



						fig = px.line(df, x = 'time', y = ['EfficientNetB0', 'AlphaNetL3'], markers=True, color_discrete_sequence = ["red", "blue"], title = "FPS vs Time")

						fig.update_layout(xaxis_title = 'Time', showlegend = True, yaxis_range = [0,5], legend_title = "Model", title_x = 0.5)
						fig.update_layout(yaxis_title = "FPS", font = dict(family = "Courier New, monospace", size = 14), autosize=False, width=1500,height=1200)
						# autoscale y axis
						fig['layout']['yaxis'].update(autorange = True)
						images_processed = 100*int(batchSize)*count
						images_processed_string = "Total number of images inferred: " + str(images_processed)
						#st.write(images_processed)
						

						try:
							placeholder.empty()
							processing_placeholder.empty()
						except:
							pass
						
						

						with right_side_column:
							placeholder = st.plotly_chart(fig)
							#processing_placeholder = st.success(images_processed_string)
							processing_placeholder = st.metric(label="Total number of images inferred", value=str(images_processed), delta=str(int(batchSize)*100))


		with tab_EfficientNetB3_AlphaNetU7:
			# st.header("EfficientNetB0")

			# renderData("100 Classes, MFLOPS = 386")

			#st.write("Please select the inference parameters")

			batchSize = st.selectbox(
				'Choose  the batchsize',
				batchsize_array, key="EfficientNetB3_AlphaNetU7_batchsize")
			modelPrecision = "FP32"
			#modelPrecision = st.radio(
			#	"",
			#	('FP32', 'FP16'), horizontal=True, label_visibility="collapsed", key="EfficientNetB3_AlphaNetU7_modelPrecision")
			cpu_gpu = "GPU"
			#cpu_gpu = st.radio(
			#	"",
			#	('CPU', 'GPU'), horizontal=True, label_visibility="collapsed", key="EfficientNetB3_AlphaNetU7_cpu_gpu")

			# model_name = "EfficientNetB0"

			# st.write('You selected:', batchSize, cpu_gpu, modelPrecision)
			st.success("Running with FP32 Precision on GPU")

			benchmark = st.button("Benchmark", key="EfficientNetB3_AlphaNetU7_benchmark")

			if benchmark:
				fps_array_efficientnet_b3 = []
				fps_array_AlphaNetU7 = []
				time_array = []
				if cpu_gpu == "CPU":
					cpu_gpu = 'cpu'
				else:
					cpu_gpu = 'cuda'
				count = 0
				stop_button = False
				stop_button = st.button("Stop")
				while (stop_button == False):
					with st.spinner("Processing..."):
						count = count + 1
						
						all_result_efficientnet_b3, mflops_efficientnet_b3, mparam_efficientnet_b3 = inference_efficientnet_b3(
							int(batchSize), cpu_gpu)
						fps_efficientnet_b3 = int(all_result_efficientnet_b3)
						fps_array_efficientnet_b3.append(int(fps_efficientnet_b3))

						singaporeTz = pytz.timezone("Asia/Singapore")
						now = datetime.now(singaporeTz)
						current_time = now.strftime("%H:%M:%S")
						time_array.append(current_time)


						
						all_result_AlphaNetU7, mflops_AlphaNetU7, mparam_AlphaNetU7 = inference_alphanet_u7(
							int(batchSize), cpu_gpu)
						fps_AlphaNetU7 = int(all_result_AlphaNetU7)
						fps_array_AlphaNetU7.append(int(fps_AlphaNetU7))


						try:
							info_placeholder_1.empty()
							info_placeholder_2.empty()
							fps_placeholder.empty()
						# fps_placeholder = st.success("EfficientNetB0 and Hybrid FPS on the currrent batch is " + str(int(fps_effb0)) + " and " + str(int(fps_hybrid)) + " respectively.")
						except:
							pass
						
						info_placeholder_1 = st.info(
							str("EfficientNetB3 - " + "MFLOPS - " + str(mflops_efficientnet_b3) + " , " + "MPARAM - " + str(mparam_efficientnet_b3)))

						info_placeholder_2 = st.info(
							str("AlphaNetU7 (Improved Sampling – Uniform Flop) + Hybrid (0.230) - " + "MFLOPS - " + str(mflops_AlphaNetU7) + " , " + "MPARAM - " + str(mparam_AlphaNetU7)))


						fps_placeholder = st.success("EfficientNetB3 and AlphaNetU7 FPS on the currrent batch is " + str(int(fps_efficientnet_b3)) + " and " + str(int(fps_AlphaNetU7)) + " respectively.")

						
						
						fps_array_effb3_np = np.array(fps_array_efficientnet_b3)
						fps_array_hybrid_np = np.array(fps_array_AlphaNetU7)
						time_array_np = np.array(time_array)

						df = pd.DataFrame({'EfficientNetB3':fps_array_effb3_np, 'AlphaNetU7':fps_array_hybrid_np, 'time': time_array_np})

						# st.write(df)



						fig = px.line(df, x = 'time', y = ['EfficientNetB3', 'AlphaNetU7'], markers=True, color_discrete_sequence = ["red", "blue"], title = "FPS vs Time")

						fig.update_layout(xaxis_title = 'Time', showlegend = True, yaxis_range = [0,5], legend_title = "Model", title_x = 0.5)
						fig.update_layout(yaxis_title = "FPS", font = dict(family = "Courier New, monospace", size = 14))
						fig.update_layout(
						autosize=False,
						width=1500,
						height=1200,)
						# autoscale y axis
						fig['layout']['yaxis'].update(autorange = True)
						images_processed = 100*int(batchSize)*count
						images_processed_string = "Total number of images inferred: " + str(images_processed)
						
						try:
							placeholder.empty()
							processing_placeholder.empty()
						except:
							pass

						with right_side_column:
							placeholder = st.plotly_chart(fig)
							processing_placeholder = st.metric(label="Total number of images inferred", value=str(images_processed), delta=str(int(batchSize)*100))


		