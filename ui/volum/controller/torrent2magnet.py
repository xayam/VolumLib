import bencodepy
import hashlib
import base64
from collections import OrderedDict


def make_magnet_from_file(file):
    metadata = OrderedDict(bencodepy.decode_from_file(file))
    subj = metadata[b"info"]
    hashcontents = bencodepy.encode(subj)
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest).decode()
    return (
            "magnet:?"
            + "xt=urn:btih:"
            + b32hash
            + "&dn="
            + metadata[b"info"][b"name"].decode()
    )


# + '&xl=' + str(metadata[b'info'][b'length'])
# + '&tr=' + metadata[b'announce'].decode() \


if __name__ == "__main__":
    pass
    # magnet = make_magnet_from_file(
    #     "VolumLib.torrent")
    # print(magnet)
