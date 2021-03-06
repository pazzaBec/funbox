#!/usr/bin/python

import os, sys, argparse, json, getpass, random, time

class Address :
    def __init__(self, _Secret, _addr) :
        self.Secret = _Secret
        self.addr = _addr

Fee = 0.00000001
srcAddr = Address("", "UZEa2p6K4AjYyypGH7c12n7LM8s7YTQkxu")
listrcvs = [
    "UN1rcJcbB3Lv54GQzVohMKjWuuRF8ueP1Z",
    "UNXEToQZQgWiubWFyU4RxTG5ZtXtjiJAgG",
    "UNcULJh4DawVy3esG2eudu6TDhHHN4Vdwu",
    "UNdN15MS4t7ZNsjJ47Ve6zjunj9GV9wBCN",
    "UNpua3vrMWYV9efHKeAsP9fFPQWPgpqwC3",
    "UNsrd3PgDpvy65BJWBRWUnKuakyvtKu27Q",
    "UP3rUT53xZEoUbzFcVrN3a2YXAQRNsv4oE",
    "UP5r7B3nZjBJLHjF4KZosGm5onRkfbJwwa",
    "UP7j1ehgqRnbkFaELpJaiE7remrpcAyC3c",
    "UP8YxeYxvuk6kRQ37FRmoMZxaRaG1dhUrq",
    "UP9NQhGQ237MgxzCixZwSg9ZZLUSAtowuv",
    "UPAqLV6XV4qrPojW1AjtJrk31Ue9NWAuvt",
    "UPWZ2tzkPsTEQtREagrdPeUWRuD3dqekPU",
    "UPc6AWQukYHgWCET8YNvum8W8ABaCrKj81",
    "UPhj33hhpagncsPguhWjhU1exT5aRwZAeE",
    "UPr3u9Hhupe963Ga5fJcM9bFpjyuUCzVuM",
    "UQEYbDtyRMzj4QY93nLZnVhSQvqYLVVYT8",
    "UQTw6FxhF5e7JUYU14m38GZfnkhnjCZyrx",
    "UQc3r5xAxGEXpvJCbYP7QnpwT6UTc7XTVr",
    "UQuLnzXiyWW7vgZ8D6FtkSbzsuXnWr6teM",
    "UR67n2NGXePm1eXumV1VjhhDD7Poo3wacr",
    "UR6sFgxz7NLcDLSKWZY7vgBc8oG27c8nP8",
    "UR7v1e4aA4pZbnmsR59UrpHGmRkwT3G91C",
    "UR88J2L5PjpoQUnaMTMSSEAmzAbLJXA89v",
    "URB8yrQQoKWF3yFjqz4MPfPQWz7abbtThY",
    "URmvwogKVwDrVj63DMrnytgPsvSGaEumyz",
    "URqHHXf3s2cQwwSiFRT1Xhnqr7CeoH3mg6",
    "US5SwtgHY4XKWWRHapKjdgaJbczsekJ8fz",
    "USCSMdPsWbPtjcoAkJdZ3CvTVVbbh7LN2f",
    "USFZBNxTVzxe36JsQ6GUJmFf61YGT47hCM",
    "USMvrovfr8CfXMskmoPRFYcw4ABeaU1dz9",
    "USdemCBNZz97tYhzV9HcmcgYZmNpDSR7hn",
    "USptiUrLW1Gr5X5mK9Ny4mw6TG3viAMWGR",
    "UT3CXBo5GE3Tuxkn5vxzPuo4CLc68sLaqf",
    "UTAyQ32wY6Qtfw86qy5aAVd1F9SqoxQzDc",
    "UTFbn9bvHd5p5KrMDBTikYsQTBTvkCMyob",
    "UTkLhSPUBDp4yYhTBxq9ACCufcEkmzz9VQ",
    "UTpPWFPxUmTyAZZRDjM2obMN49HF3tNSHD",
    "UU3Ur9ZxGAtK8KjLNVNqK9twufDoiaKxHq",
    "UU7nNt1L9fKKAgp348eogcnA1uYy8mQ3CM",
    "UUE6SrpWrp9akVsULJmvrtHgiUWweC1tao",
    "UUHuQjSypehjCQNCLLmNx6ieEfbNr4VGJs",
    "UUJbWNe3QcZ8MXu1Ve8euHTV29bhMx41tX",
    "UUTenRzJPTKz4pVFLUhr36MFNUBXUa5sj5",
    "UUYkxdjxRPbvzaLS2p4K5RQvecCWZ27NAQ",
    "UUbRGoDASMa1QojcSDSobdG9gAfarspPS4",
    "UUyAwLRPDtwBGUAbRKDCPX5caNduewGFU8",
    "UUzJEvjuq6nadBzAKHAQsBSbocQSUBzxsr",
    "UV7odUnRNeVxBLaeYKsqx9Fb94jR5wDhAm",
    "UVDmQHh7XBF77xmHcxBjFdM64HtP624X9C",
    "UVGGWqRNm2T3it3dnYs4czJUkZgQcJ5cTN",
    "UVijTNQdP3uezR1cfFi3VwxYbwt3wSgk7N",
    "UVjjR8o5Mwcn4H7brwF1U8Kff2s11Eqpbx",
    "UVobrp9WsU5A315ekHeokGCAnLp9rLUJSY",
    "UVowx6E5Ld6yv4aVkR2XDNGKe6Tq8vgN7p",
    "UW8gnQqx6hTpEpF65z4YuWKD3fsD87Uz8o",
    "UWJEMEHjVz2NURktZZoiGJpYY3MrmRxgSy",
    "UWpoozMAn4scSuc4CfQSSg9pjC6BCmXgUk",
    "UX3WPtrfP1Kn5GC4DmUQasgrLhBtg11FtU",
    "UX4gg8mT8cBaxgHCJTTHmJdw9sGbLwQioZ",
    "UXAJDrWjAttdtnBUuvuStLqtDhZFWKa4py",
    "UXMcPNdJSrTLzahtXNz4QG3uRdALnFPwp5",
    "UXPDSjaojQThHHZX5LvJyVn5LdiFK8hyCg",
    "UXQ8oFgPjdce6LbiU1jJWp4QwHx75w6cnV",
    "UXRAVdt9B3LYuMhWzRuchEjXi94ewiSARN",
    "UXRwUzBituM2ULMjKXCvdihdLzJYKHN8TR",
    "UXT1hNa4MLXEJ8Y58CiCoKggrid75Ep2MM",
    "UYCqoJfMegCpP9fjzH8KgKTr9jU8ANFSvR",
    "UYXBU8gbT1w5cSEtqYFjjzcjJmgNqHmKY2",
    "UYgGNVNbaGaRJxsQdSQAgWMZ6ZnB8K6eNh",
    "UYr3WTzLvDLMHbRErwfw7pZnDmDgS4RCXk",
    "UYtKfCukSYAtipan4z19A574j2HUHSfi1X",
    "UYu9YBPnE4ksbcwoMVdaDiHkhwnNtCBm6M",
    "UZ3DoDruo6EmTBFgj4xeehkg65v8Xzozt6",
    "UZ9tSwM2oZYGxLAJGyCUMCJnWeaxuVQQoV",
    "UZRBX4wrUayQDUs7nCcCZWv5MKbYr6FGZk",
    "UZh5SViMB2NziYn3wXCPuLgQsTGZaPUtZf",
    "UZr1FmBertbDg6TgUcbqyS4FY75PdxMVtJ",
    "UZv5JioSMgQD1FvFVCzjqioCkiit6J63DG",
    "UZvCPytFuiKojKRHFLfPGiYMVUYARLaxoB",
    "Ua2245WFkLdMeJZqvWy5DVLkBWTo3mK2Ad",
    "UaELb6wxJQWHdjovtctcCxknhge5G7fhGs",
    "UaTRDMgLHgZhxEanHQyYnXLSSnwBxxtkXw",
    "UavWkHEdZg49e772uzt8uYyHKqN6GVWVej",
    "UazXtDKKhE3wjUnm8FjVsjJ5hpieDTqHHA",
    "UbAbJbJMaHabXgQQ1WTLQEXgv1RX7mdJii",
    "UbTSQcedwKBS9yXwmpsDN5PdNbjcZdBqRQ",
    "UbpUsDEBmEwsHYqbApLH3T9QWaWvtG6Yfv",
    "Uchinf8oZicyq9bRwu3xs9bw3ttbPPkpJn",
    "UckA8pT2i5XnbvALtVTR8EZ6h2XR5VXkkc",
    "UckGNnCh24tSyqMnbLtxX71oG24srv2hg1",
    "Ucmo5UWoyoACAMTPUVLjB6VcXPF1xVU8H1",
    "Ucpf65g571ZGDRa5DPLpbyVPvpuLBUPBxB",
    "Ud6ieyoJsUFiPVJ1nrnAdthiMn8sVEp3hm",
    "Ud8fs3tuDKYPQXp9zgeJ2idzZhiVwuqfxk",
    "UdKxG6TBFqd1RgFs3RWqpfAmTLHbNeXmcN",
    "UdNg7VPdMrrftxryog6zZPaFXAfgeyvs6V",
    "UdQdTFmYPvLcbPSVt7HEsTPBSwaj1zBdk3",
    "UdWkdD7PW69qp4y8BrtzTr5UF8wBNUvGio",
    "UdiFCfHDT7HEBHsNJc4sCz6tTpuE2VoLXx",
    "UdoAkQYfmzBXtzq58YG2uBCEBuc839t4oK",
    "UeB7Em1bwkN29LPjfLwzWm98RYSf7LD4u2",
    "UeP56b2m93V9t47NYaPdsx7EnysBJCxK9N",
    "UeVujUDieAos3REVZg5JFjQtAGyqYoAgkS",
    "UecfP7yeX4ZEYqLKgDWkyRiEBW29iCMY75",
    "UehyQhdvcdA4aN2LtX9Rip5nmnncjZBGrY",
    "UeihASZXoWKbn5ceMC8yjVGV64cmD1KbYD",
    "Uemn7km53jDRAtyUpJqp72TPfTjr1r5NLW",
    "UewvdbfisHcrXC75U7RcTUGueEF4J2Hxo7",
    "Uf8ijZQuCo9T5adU2cA8Zo2wkdt41uGXSP",
    "UfSHkY7GH54fMrL5irGFxGZkwQLYZ1KsAU",
    "UfSbnuAm34RY1jXcqYKPfzK9c2HGemEkgi",
    "UfYuyUyxCHJazSnPaSg58LGEW2QT7j521T",
    "UfaARhMz9qqbgEQVgSydfGn474EA9KzoZz",
    "UfaBGb2DqLJCN4nHYaQ11THy4CYNMaZfCh",
    "UfkPmZA4dp9efBwq2FvoDsvv7uqL1ZrDaQ",
    "UfuRmu9sgZaAHxWsKuZRLacnDpCWwywD9q",
    "UgEobJaeC2sK2ogPSKjygoPpqVqT3JCZvW",
    "UgKnZCRJLFXdcDGuZHHwj9rVRRNjHbRaVm",
    "UgL4CmohRaRy4b1UJkpzHaM4sTN5hxTHpK",
    "UgME26kmSzWAjuSK173bkdmcyBs9Awf3Tw",
    "UgZ75ytgL1CQUDWYHFmDKbeq33AEG7Axxd",
    "UgdLkuSMFJ2X5mwbpNtKwsDVe92eEHCXkR",
    "UgkQc1sM9UyaVzZMD9oFa2F8ukvdXL4XhJ",
    "UguZJMdnCViGE1x6RMW8L6ezJxSxB4xrDP",
    "UgvTjPUFvx8bXgjrT129DgfGMkihwDdZzS",
    "Uh1g3R6EoqZKZHX4SS65d54yahiuj7TzWP",
    "UhCMPSNmUdZxk9EkQVCwjszPybkQuWL5Uz",
    "UhRbyQTrxjaXcDTwa4Ez6vruBnwxJfTJyH",
    "UhpTpG59UxKUerC9bj1pYic1xyrB74U97i",
    "Ui1e3VXn2UBjzujrhdSgggTStDiLbsEqPq",
    "UiEVRVonZVRkRhDvCPdoYPHrvDiogBoD3X",
    "UiHG9Xi37AoQZEusbokfiHMMAYEtmPdDiL",
    "UiJQe4fXvT2oNtF4FggagFNVvKegjBfYXL",
    "UiSZgxC6Y4rAto7vuouh1sKRQqAauZ34k4",
    "UiUWNJ8CGgJdrHqDFbPCsscXxo9fq3ucov",
    "UihrbyDZyuS4YpvQEqvZ6UeLaT9DqT2xjs",
    "UikqacmnLRAkeFH9t9L9GRwmBDJ7nPV663",
    "UipoX6NfhnoKtnNqaGPVH9TYURq7qBkEP8",
    "UiqeFZVDAQjfHwR8oyXdDJaNtJ7Yj2sQGQ",
    "UiviybGHHWPmnZ12HiD6H2S6tprzMvQ1dY",
    "UjHvH1Tz9kpthdHdv8MfxLQvqsHutenRyT",
    "UjNPEktAcne2T9dTZPvNFnprjC1KWo2AQp",
    "UjVFEhrbhovGrboj1wrPtxL62eZygXcXLZ",
    "Uja9PiTwn7bNigTpC4RNkVsSvE8bpjrPZp",
    "UjeNLwBZrSGNUhSh8sAXrogwKdpxYhQaU7",
    "Uk3XcNq9rUZp2T7UBmuEeK1anZYMF7LXVD",
    "UkXkizAXtamVLTSjMyJfBbMwifh2HMeZeS",
    "UkmJw4gEQmFqC8gnxJ1YHpivWQ2q9nJuXB",
    "UktV55yQbJidyMhT77vmPLPawUxzm66AMq",
    "Um1Ly711geL1UzDGevff1sTDdQ4fK4DDTE",
    "Um3opW8KhrXCXcQuu3vofnZ56h4XwZj6ud",
    "Um9NP7awCLh3XNZx6cZ5moFnMoBhDZ4MTf",
    "UmAZDxQZFHnngp7bsydMExaUXehN2Pz5hn",
    "UmGfn2TBx1cA3fCo2xu3xunNHWsxuzQM24"]
listIndex = 0
COIN = 100000000

def rpcwd(_m, *_params):
    _ps = ''
    for _p in _params:
        _ps += '%s,'%_p
    if _ps[len(_ps)-1] == ',':
        _ps = _ps[:len(_ps)-1]
    return 'curl -s --user Ulord130:Ulord130 --data-binary \'{"jsonrpc": "1.0", "id":"ut", "method": "%s", "params": [%s] }\' -H \'content-type: text/plain;\' http://182.151.30.93:9889/'%(_m, _ps)

def operation (_cmd) :
    _p = os.popen(_cmd)
    _data = _p.read()
    _p.close()
    return _data

def callRpc(_wd):
    ret = json.loads(operation(_wd))
    if not ret['error'] is None:
        print(ret['error'])
        os._exit(0)
    return ret['result']

def GetUtxos(_addr) :
    return callRpc(rpcwd('getaddressutxos', '{"addresses": ["%s"]}'%_addr))

def GetMemPooltx(_addr) :
    return callRpc(rpcwd('getaddressmempool', '{"addresses": ["%s"]}'%_addr))

def GetBalance(_addr) :
    return callRpc(rpcwd('getaddressbalance', '{"addresses": ["%s"]}'%_addr))["balance"]

def GetAmount() :
    return random.randint(500,10000)

def CheckUtxo(_addr, _utxo) :
    _txid = _utxo["txid"]
    if _utxo["comfirms"] < 1 :
        return False
    _pools = GetMemPooltx(_addr)
    for _memtx in _pools :
        if _txid == _memtx["prevtxid"] :
            print("conflict tx: %s"%_txid)
            return False
    return True

def GetVin(_addr, _num) :
    _vins = "["
    _utxos = GetUtxos(_addr)
    if _num > len(_utxos) :
        _num = len(_utxos)
    if _num == 0 :
        return "", 0
    _count = 0
    for i in range(0, _num) :
        _utxo = _utxos[i]
        if CheckUtxo(_addr, _utxo) == False :
            continue
        _b = _utxo["satoshis"]
        _vins += "{\"txid\":\"%s\",\"vout\":%d},"%(_utxo["txid"], int(_utxo["outputIndex"]))
        _count += _b
    _vins = _vins[:len(_vins)-1] + "]"
    return _vins, _count/COIN

def GetVout(_src, _amount) :
    _index = random.randint(0, len(listrcvs))
    _vout = "{"
    for i in range(0, 20) :
        _value = GetAmount()
        if _value >= _amount :
            break
        _vout += "\"%s\":%d,"%(listrcvs[_index], _value)
        _amount -= _value
        _index += 1
        if _index >= len(listrcvs) :
            _index = 0

    if _amount > Fee :
        _change = _amount - Fee
        #print(_amount, Fee, _change)
        _vout += "\"%s\":%.8f,"%(_src, _change)
    _vout = _vout[:len(_vout)-1] + "}"
    return _vout

def createrawtx(_vin, _vout) :
    _rawtx = rpcwd('createrawtransaction', _vin, _vout)
    print(_rawtx)
    return callRpc(_rawtx)

def signrawtx(_rawtx, _key) :
    if _rawtx == None or _rawtx == "" :
        return None
    _cmd = rpcwd('signrawtransaction', '"%s"'%_rawtx.strip('\n'), '[]', '["%s"]'%_key)
    _r = callRpc(_cmd)
    if _r["complete"] == True:
        return _r["hex"]
    print("Sign rawtransaction failed, without matched private key.")
    os._exit(0)

def sendrawtx(_tx):
    if _tx == None:
        return "No rawtransaction data"
    #return operation('%s sendrawtransaction %s'%(ut, _tx.strip('\n')))
    return callRpc(rpcwd('sendrawtransaction', '"%s"'%_tx.strip('\n')))

def run() :
    while True :
        vin, amount = GetVin(srcAddr.addr, 5)
        if amount > 0 :
            vout = GetVout(srcAddr.addr, amount)
            rawtx = createrawtx(vin, vout)
            tx = signrawtx(rawtx, srcAddr.Secret)
            ret = sendrawtx(tx)
            print(ret)
        else :
            #print(GetUtxos(srcAddr.addr))
            print("No UTXO!")
        time.sleep(60)

run()
#print(GetMemPooltx(srcAddr.addr))