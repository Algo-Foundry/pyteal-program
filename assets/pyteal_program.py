# Add directory to path so that algobpy can be imported
import sys
sys.path.insert(0,'.')

from algobpy.parse import parse_params
from pyteal import *

def main(RECEIVER_1, RECEIVER_2):

    receiver_1_checks = And(
        Arg(0) == Bytes("rcv1password"), #rcv1 password
        Txn.amount() <= Int(5000000) #5 Algos 
    )

    receiver_2_checks = And(
        Arg(0) == Bytes("rcv2password"), #rcv2 password
        Txn.amount() <= Int(10000000) #10 Algos 
    )

    receiver_checks = Cond(
        [Txn.receiver() == Addr(RECEIVER_1), receiver_1_checks],
        [Txn.receiver() == Addr(RECEIVER_2), receiver_2_checks]
    )

    program = And(
        Txn.rekey_to() == Global.zero_address(),
        Txn.close_remainder_to() == Global.zero_address(),
        receiver_checks
    )

    return program

if __name__ == "__main__":
    # Default receiver address used if params are not supplied when deploying this contract
    params = {
        "RECEIVER_1": "R4VDREHBHVETKRPBZT6IDOQQL4FBHLBYQBQQJPIBXLTCVXYJX7Z5WLDSZY",
        "RECEIVER_2": "WRBVLPUHQZ5O2UIZAKYKKMOUSNPOFIL6ALUZQZLHBDUSIKXHAEEIELWBFQ",
    }

    # Overwrite params if sys.argv[1] is passed
    if(len(sys.argv) > 1):
        params = parse_params(sys.argv[1], params)

    print(compileTeal(main(params["RECEIVER_1"], params["RECEIVER_2"]), Mode.Signature, version=6))
