import hashlib
import asyncio
from shade_agent import (
    agent,
    agent_account_id,
    agent_info,
    agent_call,
    agent_view,
    request_signature,
    ContractArgs,
    SignatureKeyType
)


async def test_agent_account_id():
    res = await agent_account_id()
    print(res)


async def test_agent_info():
    res = await agent_info()
    print(res)


async def test_add_key_not_allowed():
    res = await agent('addKey', {})
    print(res)


async def test_get_state():
    res = await agent('getState')
    print(res)


async def test_get_balance():
    res = await agent('getBalance')
    print(res)


async def test_view():
    account_id = (await agent_account_id())['accountId']
    
    res = await agent_view(ContractArgs(
        method_name='get_agent',
        args={'account_id': account_id}
    ))
    print(res)


async def test_call():
    path = 'foo'
    payload = hashlib.sha256(b'testing').hexdigest()
    
    res = await agent_call(ContractArgs(
        method_name='request_signature',
        args={
            'path': path,
            'payload': payload,
            'key_type': 'Eddsa'
        }
    ))
    print(res)


async def test_sign():
    path = 'foo'
    payload = hashlib.sha256(b'testing').hexdigest().zfill(2)
    
    res = await request_signature(path, payload)
    print(res)


async def test_sign_eddsa():
    path = 'foo'
    payload = hashlib.sha256(b'testing').hexdigest().zfill(2)
    
    res = await request_signature(path, payload, 'Eddsa')
    print(res)


async def run():
    await test_agent_account_id()
    await test_agent_info()
    await test_add_key_not_allowed()
    await test_get_state()
    await test_get_balance()
    await test_view()
    await test_call()
    await asyncio.sleep(2)
    await test_sign()
    await asyncio.sleep(2)
    await test_sign_eddsa()
    
    return True


if __name__ == "__main__":
    asyncio.run(run())
