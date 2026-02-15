"""Local registry command line; no hosted service or automatic jobs."""
import argparse,json
from .registry_training import train_registry
from .registry_export import export_registry
from .registry_experiments import run_registry_grid
from .io import write_json
def main():
    p=argparse.ArgumentParser(description='Synthetic patient registry experiments');sub=p.add_subparsers(dest='command',required=True)
    tr=sub.add_parser('train');tr.add_argument('--model',default='logistic');tr.add_argument('--seed',type=int,default=42);tr.add_argument('--horizon',type=int,default=30);tr.add_argument('--output',default='outputs/registry')
    ex=sub.add_parser('export');ex.add_argument('--output',default='outputs/registry_features.csv');ex.add_argument('--horizon',type=int,default=30)
    gr=sub.add_parser('grid');gr.add_argument('--limit',type=int);gr.add_argument('--output',default='outputs/registry_grid.json')
    args=p.parse_args()
    if args.command=='train':print(json.dumps(train_registry(args.model,args.seed,args.horizon,args.output)[1],indent=2))
    elif args.command=='export':print('Rows exported:',export_registry(args.output,args.horizon))
    else:
        result=run_registry_grid(args.limit);write_json(args.output,result);print('Validation experiments:',len(result))
if __name__=='__main__':main()
