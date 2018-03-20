import binascii
from neo.IO.Helper import Helper
from neo.Utils.BlockchainFixtureTestCase import BlockchainFixtureTestCase
from neo.Settings import settings
import os

class SmartContractTest2(BlockchainFixtureTestCase):

    @classmethod
    def leveldb_testpath(self):
        return os.path.join(settings.DATA_DIR_PATH, 'fixtures/test_chain')

    tbblock = b'00000000b314cf7c6e0c90a92e8383b9747aa79c5ddfcf7737b207a488731b892b2488d51524d12021655aa34c73c55ee29bfbae137bedabee8fc4c40eb0694af50dff5345b0265948f20000af83aa0714cae273f3812db982f3b0089a21a278988efeec6a027b2501fd4501403a9db02b316cf8df54ca943ffb8d929b0720bd6a9f6038385cf1784ae985eb719f37203e83757e5050e353c3f421bb1773b42a5f51d8fa6e3c3ddbfb47e8127b409e48557e491217cc989ac554dc366a866a134ecb59a1e5cfa8035b65210e7894f85bd7ae331970e66fe3fe53215234d14f7ceb61e93de0a5d660cd127814c42e40df58fe60e9aabf28f50b8cfd025d60f59550c8ab938bb9ad45956b64cbec99588059ca27197f29905e8ea9d441eb540540ce8ecd2c33e4c2dc0c3f42f9a514a040e25ef0af821f728b7660a2e6cdfff4fc9e450a49f7b15e0ceaa346444a7e3a2f21c527b922a4a3b392a0cdd302c2061404cc01f41ff80fc5ff391ee11d5f6a0540477217f35f0f54107aacce5893cdf5307645284969865148ffc2c8ae068b4791b7b975c724c54096c423ab35662be44696c01edf0c50e04b52500cbb00889db5f155210209e7fd41dfb5c2f8dc72eb30358ac100ea8c72da18847befe06eade68cebfcb9210327da12b5c40200e9f65569476bbff2218da4f32548ff43b6387ec1416a231ee821034ff5ceeac41acf22cd5ed2da17a6df4dd8358fcb2bfb1a43208ad0feaab2746b21026ce35b29147ad09e4afe4ec4a7319095f08198fa8babbe3c56e970b143528d2221038dddc06ce687677a53d54f096d2591ba2302068cf123c1f2d75c2dddc542557921039dafd8571a641058ccc832c5e2111ea39b09c0bde36050914384f7a48bce9bf92102d02b1873a0863cd042cc717da31cea0d7cf9db32b74d4c72c01b0011503e2e2257ae030000af83aa07000001e72d286979ee6cb1b7e65dfddfb2e384100b8d148e7758de42e4168b71792c6000e1f505000000002fd260068454cf8060f8eac10b89e7da907f3bf100d101fd42011467f97110a66136d38badc7b9f88eab013027ce49681f416e745368617265732e426c6f636b636861696e2e4765744163636f756e74210327da12b5c40200e9f65569476bbff2218da4f32548ff43b6387ec1416a231ee821026ce35b29147ad09e4afe4ec4a7319095f08198fa8babbe3c56e970b143528d22210209e7fd41dfb5c2f8dc72eb30358ac100ea8c72da18847befe06eade68cebfcb921039dafd8571a641058ccc832c5e2111ea39b09c0bde36050914384f7a48bce9bf921038dddc06ce687677a53d54f096d2591ba2302068cf123c1f2d75c2dddc54255792102d02b1873a0863cd042cc717da31cea0d7cf9db32b74d4c72c01b0011503e2e2221034ff5ceeac41acf22cd5ed2da17a6df4dd8358fcb2bfb1a43208ad0feaab2746b57c1681a416e745368617265732e4163636f756e742e536574566f7465730000000000000000012067f97110a66136d38badc7b9f88eab013027ce4901c5504d21fce894ed8bb2c01724522a0785133894d947419f81cc582bf0a3fa56000001e72d286979ee6cb1b7e65dfddfb2e384100b8d148e7758de42e4168b71792c600051a1605601000067f97110a66136d38badc7b9f88eab013027ce4901414039b76a3a28ee1551e2a998cd8bd213af2e1aef7ccbe962be3ee12a00e20f183ca908f8165dd953fea998febad466ee81ab6de0020f28607e4db82376a9e25df22321034b44ed9c8a88fb2497b6b57206cc08edd42c5614bd1fee790e5b795dee0f4e11ac80000002fdc633307f941a56dcac49d4bb312721d6d7e61d138d7268a8de36ac35d35ed100007bed0122423fed8c4e7077682adf30e4496fe274e469122fe2cf1e42e61cce780400039b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc5005cb2ec220000008e568bcbf3bab3d524f556a78148d462c0be7383ea51659358737b6f2b344ee09711d438d03d75d6ea7f48792024a5528ea0b7bb00c029f73d540500087e0cd7ca61e34c48c1f443d1a323c60c183235ea51659358737b6f2b344ee09711d438d03d75d6ea7f48792024a5528ea0b7bb0080c6a47e8d03008e568bcbf3bab3d524f556a78148d462c0be738302414029dd904ba683e33662821c80df050ef3dff077aa83f6f6f53c77db314b82560d9118872e27906077719690a04625d3943b35bfe88d0d252b05979e871fa6cf9a9f0210270021039b2c6b8a8838595b8ebcc67bbc85cec78d805d56890e9a0d71bcae89664339d6209b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc520ea51659358737b6f2b344ee09711d438d03d75d6ea7f48792024a5528ea0b7bb2102956593708a81bc6b64e66b1ba10a24eace9273f7a2945c746e604da2969a9f9f67e33448f4120cd2fd3d2ed7ade6c81ed065284d8a4140640d2af783c8ac5be5e7a4639212be8f94a762bd3523a5800e51c44cee402d2184018f1192521bb7a43dd55048e3979a1e060fdd7b574c1dcdc22e751bcecadf2321039b2c6b8a8838595b8ebcc67bbc85cec78d805d56890e9a0d71bcae89664339d6ac'

    def test_b_invocation(self):

        hexdata = binascii.unhexlify(self.tbblock)

        block = Helper.AsSerializableWithType(hexdata, 'neo.Core.Block.Block')

        json = block.ToJson()

        self.assertIsNotNone(json)

        result = self._blockchain.Persist(block)

        self.assertTrue(result)
