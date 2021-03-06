import sys 
import viewpoints
import model
import candidates
import path_inflation

viewpoints_file = 'viewpoints.csv'
model_file = 'models.csv'
candidates_file = 'candidates.csv'

if __name__ == '__main__':
	print('Before running the code, fill alps/config/query_google_key.info with your own google key')
	if len(sys.argv) < 5:
		print('Wrong argv! Should be \'$python run.py lat_top lat_bot lon_left lon_right\'')
		sys.exit(0)

	print('====== generating SV viewpoints ======')
	viewpoints.run(map(float, sys.argv[1:]))

	print('====== generating 3D model ======')
	model.run(viewpoints_file)
	
	print('====== generating candidates ======')
	candidates.run(model_file)
	
	print('====== computing path inflation ======')
	print('This part is slow, you can split the candidate file and use multi-processing to speedup')
	path_inflation.run(candidates_file)	
	
	print('done')
